# problem description: https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # k is the row number of what you want to exam
        
 #   def exam_rows(board):
        mistake = 0
        # set a list with no dots
        for k in range(9):
            # I made a mistake, exam every line should initialize the no_dots_list
            no_dots_list = []
            for i in range(9):
                if board[k][i] != '.':
                    no_dots_list.append(board[k][i])
        # exam whether no_dots_list have duplicates, every row take a exam
            if len(no_dots_list) == len(set(no_dots_list)):
                right = 1
            else:
        # add indicator
                mistake = 1
                break
                
        if mistake == 1:
            return False
 #   def exam_columns(board):
        
        # set a list with no dots
        for k in range(9):
            no_dots_list = []
            for i in range(9):
                if board[i][k] != '.':
                    no_dots_list.append(board[i][k])
        # exam whether no_dots_list have duplicates, every column take a exam
            if len(no_dots_list) == len(set(no_dots_list)):
                right = 1 
            else:
                mistake = 1
                break
        if mistake == 1:
            return False

  #  def exam_nine_area(board):
        # different iterative method
        #have 9 area need to exam
        for area in range(9):
            no_dots_area_list = []
            # I made another mistake, I don't assign the start position of the column and row
            # I also forget area in range(0,9), not range(1,10),(1,10) is experimental
            # Third mistake, the upper limitation of row range should be 3*(area//3)+3, not 3*(area//3)+2
            for row in range(3*(area//3), 3*(area//3)+3):
                
                for column in range(3*(area%3), 3*(area%3)+3):
                    if board[row][column] != '.':
                        no_dots_area_list.append(board[row][column])
            if len(no_dots_area_list) == len(set(no_dots_area_list)):
                right = 1
            else:
                mistake = 1
                break
        if mistake == 1:
            return False  
        
        
        return True                
       # exam_rows(board)    
       #exam_columns(board)    
        #exam_nine_area(board)    
            
