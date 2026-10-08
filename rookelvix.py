#!/usr/bin/env python3
"""Rookelvix: terminal chess against a simple one-ply opponent."""
import curses,argparse,random
import chess
from terminal_ui import setup,text,title
VALUES={chess.PAWN:100,chess.KNIGHT:320,chess.BISHOP:330,chess.ROOK:500,chess.QUEEN:900,chess.KING:0}
class Game:
 def __init__(self,seed=None,fen=None):self.board=chess.Board(fen) if fen else chess.Board();self.rng=random.Random(seed)
 def push(self,value):
  if self.board.is_game_over(claim_draw=True):raise ValueError('Game ended. R starts a new game.')
  try:move=self.board.parse_uci(value.strip().lower())
  except ValueError as e:raise ValueError('Use legal coordinates like e2e4 or a7a8q.') from e
  self.board.push(move)
 def outcome(self):
  o=self.board.outcome(claim_draw=True)
  if not o:return 'Check' if self.board.is_check() else 'Your move'
  return ('Draw' if o.winner is None else 'White wins' if o.winner else 'Black wins')+' ('+o.termination.name.lower()+')'
 def ai(self):
  if self.board.turn!=chess.BLACK or self.board.is_game_over(claim_draw=True):return None
  best=-10**9;choices=[]
  for move in list(self.board.legal_moves):
   self.board.push(move)
   if self.board.is_checkmate():score=10**6
   elif self.board.is_game_over(claim_draw=True):score=0
   else:score=sum(VALUES[p.piece_type]*(1 if p.color==chess.BLACK else -1) for p in self.board.piece_map().values())+(20 if self.board.is_check() else 0)
   self.board.pop()
   if score>best:best=score;choices=[move]
   elif score==best:choices.append(move)
  move=self.rng.choice(choices);self.board.push(move);return move.uci()
def run(stdscr,seed):
 setup(stdscr);g=Game(seed);buf='';message='You are White. Lowercase black pieces, uppercase white.'
 while True:
  title(stdscr,'Rookelvix',g.outcome(),'Type e2e4 + Enter | promotion e7e8q | R restart | Q quit')
  h,w=stdscr.getmaxyx()
  if h<18 or w<68:text(stdscr,4,2,'Resize to 68x18. Position retained.',3)
  else:
   for rank in range(7,-1,-1):
    text(stdscr,4+7-rank,3,rank+1,1)
    for f in range(8):
     piece=g.board.piece_at(chess.square(f,rank));text(stdscr,4+7-rank,6+f*4,' '+(piece.symbol() if piece else '.')+' ',4 if piece and piece.color else 2,True)
   text(stdscr,12,6,' a   b   c   d   e   f   g   h',1);text(stdscr,14,2,'Move: '+buf,1);text(stdscr,15,2,message)
  stdscr.refresh();k=stdscr.getch()
  if k==ord('q') and not buf:return
  if k==ord('r') and not buf:g=Game(seed);message='New game.';continue
  if h<18 or w<68:continue
  if k in (curses.KEY_BACKSPACE,127,8):buf=buf[:-1]
  elif k in (10,13):
   try:g.push(buf);reply=g.ai();message='Black: '+reply if reply else g.outcome()
   except ValueError as e:message=str(e)
   buf=''
  elif 32<=k<127 and chr(k).lower() in 'abcdefgh12345678qrbn' and len(buf)<5:buf+=chr(k)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--seed',type=int);p.add_argument('--demo',action='store_true');a=p.parse_args()
 if a.demo:print('ROOKELVIX\n'+str(Game(a.seed).board));return
 try:curses.wrapper(run,a.seed)
 except curses.error:print('Needs an interactive curses terminal (68x18 minimum).');return 2
 except KeyboardInterrupt:pass
if __name__=='__main__':raise SystemExit(main())
