import unittest,chess
from rookelvix import Game
class Tests(unittest.TestCase):
 def test_start(self):self.assertEqual(len(list(Game().board.legal_moves)),20)
 def test_illegal(self):
  g=Game();self.assertRaises(ValueError,g.push,'e2e5');self.assertEqual(g.board.fen(),chess.Board().fen())
 def test_ai(self):
  g=Game(1);g.push('e2e4');legal=list(g.board.legal_moves);m=g.ai();self.assertIn(chess.Move.from_uci(m),legal);self.assertTrue(g.board.turn)
 def test_castle(self):
  g=Game(fen='r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1');g.push('e1g1');self.assertEqual(g.board.piece_at(chess.F1).piece_type,chess.ROOK)
 def test_enpassant(self):
  g=Game()
  for m in ('e2e4','a7a6','e4e5','d7d5','e5d6'):g.push(m)
  self.assertIsNone(g.board.piece_at(chess.D5))
 def test_promote(self):
  g=Game(fen='7k/P7/8/8/8/8/8/7K w - - 0 1');g.push('a7a8q');self.assertEqual(g.board.piece_at(chess.A8).piece_type,chess.QUEEN)
 def test_mate(self):
  g=Game()
  for m in ('f2f3','e7e5','g2g4','d8h4'):g.push(m)
  self.assertIn('Black wins',g.outcome());self.assertIsNone(g.ai());self.assertRaises(ValueError,g.push,'a2a3')
 def test_draw(self):self.assertIn('Draw',Game(fen='7k/8/8/8/8/8/8/K7 w - - 0 1').outcome())
 def test_stalemate(self):self.assertIn('stalemate',Game(fen='7k/5Q2/6K1/8/8/8/8/8 b - - 0 1').outcome())
 def test_legal_random_games(self):
  for s in range(3):
   g=Game(s)
   for _ in range(20):
    if g.board.is_game_over(claim_draw=True):break
    g.board.push(g.rng.choice(list(g.board.legal_moves)));g.ai();self.assertTrue(g.board.is_valid())
if __name__=='__main__':unittest.main()
