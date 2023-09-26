from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
from tkinter import *
 
def clearAll() :
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    negativeField.delete(0, END)
    overallField.delete(0, END)
 
    textArea.delete(1.0, END)
     
def detect_sentiment(): 
    sentence = textArea.get("1.0", "end")
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
    string = str(sentiment_dict['neg']*100) + "% Negative"
    negativeField.insert(10, string)
      
    string = str(sentiment_dict['neu']*100) + "% Neutral"
    neutralField.insert(10, string) 
    string = str(sentiment_dict['pos']*100) +"% Positive"
    positiveField.insert(10, string)
     
    if sentiment_dict['compound'] >= 0.05 :
        string = "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        string = "Negative"
       
    else :
        string = "Neutral"
 
    overallField.insert(10, string)
         
if __name__ == "__main__" :
     
 
    gui = Tk()
     
    gui.config(background =  "#856ff8")
 
    gui.title("Sentiment Analysis")
 
    gui.geometry("375x500")
 
    enterText = Label(gui, text = "Write Your Comments Here",bg = "#856ff8",borderwidth=7,)
 
    textArea = Text(gui, height = 11, width = 35, font = "lucida 13",borderwidth=9,relief=SUNKEN)
 
    check = Button(gui, text = "Check Sentiment", fg = "Black",
    bg = "light blue", command = detect_sentiment,relief=SUNKEN)
 
    negative = Label(gui, text = "Sentence was rated as: ",
    bg = "#856ff8",relief=SUNKEN)
   
    neutral = Label(gui, text = "Sentence was rated as: ",
    bg = "#856ff8",relief=SUNKEN)
   
    positive = Label(gui, text = "Sentence was rated as: ",
    bg = "#856ff8",relief=SUNKEN)
 
    overall = Label(gui, text = "Sentence Overall Rated As: ",
    bg = "#856ff8",relief=SUNKEN)
 
    negativeField = Entry(gui)
    neutralField = Entry(gui)
    positiveField = Entry(gui)
    overallField = Entry(gui)
 
    clear = Button(gui, text = "Clear", fg = "Black",
    bg = "light blue", command = clearAll,relief=SUNKEN)
     
    Exit = Button(gui, text = "Exit", fg = "Black",
    bg = "light blue", command = exit,relief=SUNKEN)
 
    enterText.grid(row = 0, column = 2)
     
    textArea.grid(row = 1, column = 2, padx = 30, sticky = W)
     
    check.grid(row = 2, column = 2)
     
    negative.grid(row = 3, column = 2)
     
    neutral.grid(row = 5, column = 2)
     
    positive.grid(row = 7, column = 2)
     
    overall.grid(row = 9, column = 2)
     
    negativeField.grid(row = 4, column = 2)
 
    neutralField.grid(row = 6, column = 2)
                       
    positiveField.grid(row = 8, column = 2)
     
    overallField.grid(row = 10, column = 2)
     
    clear.grid(row = 11, column = 2)
     
    Exit.grid(row = 12, column = 2)
 
    gui.mainloop()