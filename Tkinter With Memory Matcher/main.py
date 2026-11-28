import random
import tkinter as tk

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Matcher")
        # self.symbols = ["A"]
        self.symbols = list("AABBCCDDEEFFGGHH")
        random.shuffle(self.symbols)
        self.buttons = []
        self.flipped = []
        self.matched = set()
        self.clicks = 0
        self.root.config(bg="#f0f0f0")
        self.build_ui()

    def build_ui(self):

        self.click_label = tk.Label(
            self.root,
            text="Clicks: 0",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#333"
        )
        # self.click_label = tk.Label(self.root, text="Clicks: 0")


        self.click_label.grid(row=0, column=0, columnspan=4, pady=(10, 5))
        # self.click_label.grid(row=0, column=0, columnspan=4)
        # self.click_label.grid(row=0, column=0)


        for i in range(4):
            for j in range(4):
                idx = 4 * i + j
                btn = tk.Button(
                    self.root,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 16, "bold"),
                    bg="#e0e0e0",
                    activebackground="#d0d0d0",
                    relief="flat",
                    command=lambda b=idx: self.flip(b)
                )
                # btn = tk.Button(self.root, text="", width=5, height=2, command=lambda b=idx: self.flip(b))


                # btn = tk.Button(self.root, text="", width=5, height=2)

                btn.grid(row=i+1, column=j, padx=4, pady=4, ipadx=4, ipady=4)
                # btn.grid(row=i+1, column=j)
                # btn.grid(row=i, column=j)

                self.buttons.append(btn)


        # self.btn = tk.Button(self.root, text="", width=5, height=2, command=self.flip)

        # self.btn.grid(row=0, column=0)
        
        # self.btn = tk.Button(self.root, text="", width=5, height=2)

        # self.btn = tk.Button(self.root, text="Click Me")
        # self.btn.pack()


    def flip(self, idx):
        if idx in self.matched or idx in self.flipped or len(self.flipped) == 2:
            return
        # if idx in self.flipped or len(self.flipped) == 2:
        #     return

        self.reveal_tile(idx)
        # self.buttons[idx]['text'] = self.symbols[idx]
        
        self.flipped.append(idx)

        self.clicks += 1
        self.click_label.config(text=f"Clicks: {self.clicks}")

        if len(self.flipped) == 2:
            self.root.after(500, self.check_match)
        # if len(self.flipped) == 2:
        #     self.check_match()

    # def flip(self):
    #     self.btn.config(text=self.symbols[0])

    def reveal_tile(self, idx):
        self.buttons[idx]['text'] = self.symbols[idx]

    def check_match(self):
        a, b = self.flipped
        if self.symbols[a] != self.symbols[b]:
            self.buttons[a]['text'] = ""
            self.buttons[b]['text'] = ""
        else:
            self.matched.update(self.flipped)
            for i in (a, b):
                self.buttons[i]['bg'] = "#90ee90"
                self.buttons[i]['activebackground'] = "#90ee90"
        self.flipped = []


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()


# root = tk.Tk()
# game = MemoryGame(root)
# root.mainloop()



# import tkinter as tk

# root = tk.Tk()

# root.title("Memory Matcher")

# root.mainloop()