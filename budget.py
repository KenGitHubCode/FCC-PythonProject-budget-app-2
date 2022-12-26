class Category:

  def __init__(self, title):
    self.title = title
    self.ledger = []

  def __str__(self):
    '''
    When the budget object is printed it should display:

    A title line of 30 characters where the name of the category is centered in a line of * characters.
    A list of the items in the ledger. Each line should show the description and amount. 
    The first 23 characters of the description should be displayed, then the amount. 
    The amount should be right aligned, contain two decimal places, 
    and display a maximum of 7 characters.
    A line displaying the category total.
    Here is an example of the output:
    
    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more foo -15.89
    Transfer to Clothing    -50.00
    Total: 923.96
    '''
    title_row_length = 30
    desc_len = 23
    amount_len = 7

    output_string = ""

    title_len = len(self.title)
    side_stars = (title_row_length - title_len) / 2

    output_string = int(side_stars) * "*" + self.title + int(
      side_stars) * "*" + "\n"

    for item in self.ledger:
      new_row = ""

      if len(item["description"]) <= desc_len:
        #print("if len(item[) <= desc_len: callded")
        new_row = new_row + item["description"]
        new_row = new_row + " " * (desc_len - len(item["description"]))
      else:
        #print("if len(item\<= desc_len: not called")
        new_row = new_row + item["description"][0:desc_len]

      amount_as_float = "{:.2f}".format(float(item["amount"]))
      if len(str(amount_as_float)) <= amount_len:
        #print("if len(item[) <= desc_len: callded")
        new_row = new_row + " " * (amount_len - len(str(amount_as_float)))
        new_row = new_row + str(amount_as_float) + "\n"
      else:
        #print("if len(item\<= desc_len: not called")
        new_row = new_row + str(amount_as_float)[0:amount_len] + "\n"

      output_string = output_string + new_row

      # for i in range(0,31):
      #   if item["description"][i] != None:
      #     new_row = new_row+ item["description"][i]
      #   else:
      #     new_row = new_row+ " "

    #output_string = output_string + item["description"] + str(item["amount"]) + "\n"
    output_string = output_string + "Total: " + str(self.get_balance())

    return output_string

  def deposit(self, amount, description=""):
    '''
    A deposit method that accepts an amount and description. 
    If no description is given, it should default to an empty string. 
    The method should append an object to the ledger list in the form of 
    {"amount": amount, "description": description}.

    '''
    #print("Deposit called with args and for: " + str(amount) + description +
    #self.title)
    self.ledger.append({"amount": amount, "description": description})
    #print("Updated ledger after deposit: " + self.title + str(self.ledger))

  def withdraw(self, amount, description=""):
    '''
      A withdraw method that is similar to the deposit method,
      but the amount passed in should be stored in the ledger
      as a negative number. If there are not enough funds,
      nothing should be added to the ledger. 
      This method should return True if the withdrawal took place, 
      and False otherwise.
  
    '''
    if self.check_funds(amount) == True:
      amount = amount * (-1)
      self.ledger.append({"amount": amount, "description": description})
      #print("Updated ledger after withdraw: " + self.title + str(self.ledger))

      return True
    else:
      return False

  def get_balance(self):
    '''
      # A  method that returns the current balance of the budget category 
      based on the deposits and withdrawals that have occurred.

    '''
    balance = float()
    for entry in self.ledger:
      balance = balance + entry["amount"]
    #print("Get balance called with result: " + str(balance))
    return balance

  def transfer(self, amount, to_account):
    '''
      # A transfer method that accepts an amount and another budget category
      as arguments. The method should add a withdrawal with the amount 
      and the description "Transfer to [Destination Budget Category]". 
      The method should then add a deposit to the other budget category
      with the amount and the description "Transfer from 
      [Source Budget Category]". If there are not enough funds, 
      nothing should be added to either ledgers. 
      This method should return True if the transfer took place, 
      and False otherwise.

    '''
    if self.check_funds(amount) == True:
      self.withdraw(amount, ("Transfer to " + to_account.title))
      to_account.deposit(amount, ("Transfer from " + self.title))
      return True
    else:
      return False

  def check_funds(self, amount):
    '''
      # A check_funds method that accepts an amount as an argument. 
      It returns False if the amount is greater than the balance of the budget
      category and returns True otherwise. 
      This method should be used by both the withdraw method 
      and transfer method.

    '''
    if (amount > self.get_balance()):
      return False
    else:
      return True


def create_spend_chart(categories):
  '''
  Besides the Category class, create a function (outside of the class) 
  called create_spend_chart that takes a list of categories as an argument.
  It should return a string that is a bar chart.

  The chart should show the percentage spent in each category passed in
  to the function. The percentage spent should be calculated only 
  with withdrawals and not with deposits. 
  Down the left side of the chart should be labels 0 - 100. 
  The "bars" in the bar chart should be made out of the "o" character. 
  The height of each bar should be rounded down to the nearest 10. 
  The horizontal line below the bars should go two spaces past the final   bar. 
  Each category name should be written vertically below the bar. 
  There should be a title at the top that says "Percentage spent by category".

  Percentage spent by category
  100|          
   90|          
   80|          
   70|          
   60| o        
   50| o        
   40| o        
   30| o        
   20| o  o     
   10| o  o  o  
    0| o  o  o  
      ----------
       F  C  A  
       o  l  u  
       o  o  t  
       d  t  o  
          h     
          i     
          n     
          g     
  
    
  '''

  cats_withdrawl_totals = []
  #go through each cat
  for cat in categories:
    single_cat_total = float()
    #add up the total negative ledger entries
    for ledger_item in cat.ledger:
      if ledger_item["amount"] < 0:
        single_cat_total = single_cat_total + float(ledger_item["amount"])
    cats_withdrawl_totals.append(single_cat_total)

  #print(cats_withdrawl_totals)

  cats_withdrawl_percent = []
  #calc % for each catagory and round to 10
  for cat_total in cats_withdrawl_totals:
    cats_withdrawl_percent.append(
      int((cat_total / sum(cats_withdrawl_totals)) * 100))

  #print(cats_withdrawl_percent)

  tic_mark = "o  "
  title = "Percentage spent by category"

  #percent grid
  text_table = []
  text_table.append(title)
  for i in range(100, -10, -10):
    string_to_append = ""
    string_to_append = string_to_append + (f"{str(i) : >3}" + "| ")

    #Add percent to row to append
    for cat_w_percent in cats_withdrawl_percent:
      #print("cat_w_percent and then i " + str(cat_w_percent) + " " + str(i))
      if cat_w_percent >= i:
        #print ("  if cat_w_percent >= i: "+ str(cat_w_percent) + " " + str(i))
        string_to_append = string_to_append + tic_mark
      else:
        string_to_append = string_to_append + "   "

    #text_table.append(f"{str(i) : >3}" + "|")
    text_table.append(string_to_append)
  text_table.append("    ----------")

  #Title length determine
  max_title_length = int()
  for cat in categories:
    if max_title_length < len(cat.title):
      max_title_length = len(cat.title)

  #Cat title letters
  for i in range(max_title_length):
    cat_row = " "
    #for cat in range(len(categories)):
    for e, elem in enumerate(categories):
      try:
        cat_row = cat_row + elem.title[i] + "  "
      except IndexError:
        cat_row = cat_row + "   "

    text_table.append(f"{' ' : >4}" + cat_row)

  return_text_table = ""
  #print each row, creating the table
  for i, row in enumerate(text_table):
    #print(row)
    if i != len(text_table) - 1:
      return_text_table = return_text_table + row + "\n"
    else:
      return_text_table = return_text_table + row
  

  return (return_text_table)
