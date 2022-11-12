from flask import Flask, render_template, redirect

board = [0] * 9
next = 1

app = Flask(__name__, static_folder="assets", template_folder="templates")


@app.route('/')
def home():
  return render_template("tictactoe.html", b=board, n=next)


@app.route('/set/<int:i>')
def setvalue(i):
  global board, next
  board[i] = next
  next = -next
  r = checkstate(board)
  if r == 0:
    return redirect('/')
  else:
    return render_template("end.html", winner=r, b=board, n=next, r=r)


def checkstate(b):
  patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
  for p in patterns:
    t = sum([b[x] for x in p])
    if (t == 3):
      return 1  # X won
    elif (t == -3):
      return -1  # O won
  r = 0
  for i in b:
    if i == 0:
      return 0  # Game still in progress
  return 2  # Draw


@app.route('/new')
def newgame():
  global board, next
  board = [0] * 9
  next = 1
  return redirect('/')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
