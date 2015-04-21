#input
# 17
# <<+>([[*]^{f}] [-]<e[t](((%)v)t)[t]>)({%} )<+>><u>
# <<[ ]a<u(y)<(c)z>{[{b}(+<z>)+[t( )]]<d><[%]a>c}>(f)>>{/}{^[f(b)]}
# <g>{<a>e(w<a>(}(-(-))(d{-}< {+}>)[{z<g[y]>}[(+)b]]) )
# ({ }<[%]/>{</<[z][b{*}]v><h>>v}{v}{h}<f>)
# ([ (+)(b[v]<%>)])<z<g>{ }[<[z<a><d{h}>]< >z>[h{z}] [x][*]]({b}v)>
# <{/(^{w )(d(t))}><f[f](c(e)<x>(a))[u]>[e[*]<g>{d}(v)]
# [{<t>z{c <[ ]x>c[d](w)(u){ }(-<*<g>>)>}{*{d}{x}}}{-}]
# <d( ){-}[ ]><[a(y)]+{/}<w> {e}[{[y{w}](<e(y)>*)e<< >y>}[/]][t{+}]
# <><u>{x}{e ([f<t>]<y>{a}{%}b</>(t<d>){+})
# [+[x]<c>][[x]y{/}]({t(f){ }[w]<w>}y{*{a}} h>)[]
# <({*}z{{h}x})(+)[t]{*<u>(d< >)<u>[{ }(e)e]{d}}>
# {b[a]}<{h}d</>>[v][[g( )]u[e]({)}uw]((b))
# [ ]{}( ({{z}f{x}}{g}c)(t{%<v>(z)}(/){e}( )<x>))
# <[%]{((-){^<(w)h>}g){h} (<*>{f} )}>[ ][v]{e[{/}v]}[t]
# [v]([[/](+(%)(+))(w)(x{t})( [a])({{%]y}d<u>[v]){a<x>}e])[c(-)}
# (<y>[[^]{e}+]([g]e<->[y])<h>[d(<{<*>x}<[*]*> ><y[e(^)]>a)]<v>)
# <-(h)[v]>{t{a}}{d}[{v{-}<b>} ][(+ {b}<*>t][([ <d><->]%)]

def is_left_bracket(c):
  if c == '(' or c == '[' or c == '{' or c == '<':
    return True
  return False

def is_right_bracket(c):
  if c == ')' or c == ']' or c == '}' or c == '>':
    return True
  return False

dict = {')':'(', ']':'[', '}':'{', '>':'<'}

n = int(input())

for i in range(0, n):
  line = input()
  stack = []
  is_ok = True

  for c in line:
    if is_left_bracket(c):
      stack.append(c)
    elif is_right_bracket(c):
      if len(stack) > 0 and stack[-1] == dict[c]:
        stack.pop()
      else:
        is_ok = False
        break
  if is_ok and len(stack) == 0:
    print("1 ", end="")
  else:
    print("0 ", end="")