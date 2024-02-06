import chess
import chess.svg
import tkinter as tk
from tkinter import messagebox
from io import BytesIO
from PIL import Image, ImageTk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")

        self.board = chess.Board()
        self.selected_square = None

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.draw_board()

        self.canvas.bind("<Button-1>", self.click_handler)

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "black"
                self.canvas.create_rectangle(
                    col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color
                )

        self.draw_pieces()

    def draw_pieces(self):
        self.canvas.delete("pieces")
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece is not None:
                filename = f"pieces/{piece.symbol()}.png"  # You need chess pieces images in a 'pieces' folder
                img = Image.open(filename)
                img = img.resize((50, 50), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.canvas.create_image(
                    chess.square_file(square) * 50,
                    (7 - chess.square_rank(square)) * 50,
                    anchor=tk.NW,
                    image=img,
                    tags=("pieces",),
                )
                self.canvas.image = img

    def click_handler(self, event):
        col = event.x // 50
        row = 7 - event.y // 50
        square = chess.square(col, row)

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece is not None and piece.color == self.board.turn:
                self.selected_square = square
                self.highlight_square(square)
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.draw_pieces()
                self.selected_square = None
                if self.board.is_checkmate():
                    messagebox.showinfo("Game Over", f"{self.board.turn} wins!")
                    self.reset_game()
            else:
                self.selected_square = None
                self.draw_pieces()

    def highlight_square(self, square):
        col = chess.square_file(square)
        row = 7 - chess.square_rank(square)
        self.canvas.create_rectangle(
            col * 50,
            row * 50,
            (col + 1) * 50,
            (row + 1) * 50,
            outline="blue",
            width=3,
            tags=("highlight",),
        )

    def reset_game(self):
        self.board.reset()
        self.draw_pieces()


if __name__ == "__main__":
    root = tk.Tk()
    chess_game = ChessGame(root)
    root.mainloop()
