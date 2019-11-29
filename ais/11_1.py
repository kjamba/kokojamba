class tic_tac_toe():
    board = list(range(1,10))

    def draw_board(self):
        print('-' * 13)
        for i in range(3):
            print ("|", self.board[0+i*3], "|", self.board[1+i*3], "|", self.board[2+i*3], "|")
        print ("-" * 13)
    
    def take_input(self, player_token):
        valid = False
        while not valid:
            player_answer = input('Куда поставим {0}?'.format(player_token))
            try:
                player_answer = int(player_answer)
            except:
                print ("Некорректный ввод. Вы уверены, что ввели число?")
                continue
            if player_answer >= 1 and player_answer <= 9:
                if (str(self.board[player_answer-1]) not in "XO"):
                    self.board[player_answer-1] = player_token
                    valid = True
                else:
                    print ("Эта клеточка уже занята")
            else:
                print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

    def check_win(self):
        win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False

    def main(self):
        counter = 0
        win = False
        while not win:
            self.draw_board()
            if counter % 2 == 0:
                self.take_input("X")
            else:
                self.take_input("O")
            counter += 1
            if counter > 4:
                tmp = self.check_win()
                if tmp:
                    print (tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print ("Ничья!")
                break
        self.draw_board()

tic_tac_toe().main()
