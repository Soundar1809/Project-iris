import pandas as pd

from sklearn import model_selection

from sklearn.neighbors import KNeighborsClassifier

from tkinter import *
import tkinter as tk 
from tkinter import filedialog


root= tk.Tk()

root.resizable(0, 0)

root.title("Iris flower Classification Prediction")


w = tk.Label(root, text="Enter the Sepal Length and width and also Petal Length and width", bg="green", fg="yellow")
w.pack(fill=tk.X)


canvas1 = tk.Canvas(root, width = 700, height = 300,  relief = 'raised', bg="violet")
canvas1.pack()

input_text = StringVar()
input_text1 = StringVar()
input_text2 = StringVar()
input_text3 = StringVar()
result = StringVar()

label1 = tk.Label(root, text='Iris Flower Prediction')
label1.config(font=('Times', 18),bg="violet")
canvas1.create_window(350, 30, window=label1)

label2 = tk.Label(root, text='Sepal length :')
label2.config(font=('helvetica', 12),bg="violet",fg="black")
canvas1.create_window(58, 90, window=label2)

entry1 = tk.Entry(root, font = ('helvetica', 12, 'bold'), textvariable = input_text, borderwidth=2)
canvas1.create_window(210, 90, window=entry1)

label3 = tk.Label(root, text='Sepal width :')
label3.config(font=('helvetica', 12),bg="violet",fg="black")
canvas1.create_window(58, 130, window=label3)

entry2 = tk.Entry (root, font = ('helvetica', 12, 'bold'), textvariable = input_text1, borderwidth=2) 
canvas1.create_window(210, 130, window=entry2)

label4 = tk.Label(root, text='Petal length :')
label4.config(font=('helvetica', 12),bg="violet",fg="black")
canvas1.create_window(400, 90, window=label4)

entry3 = tk.Entry (root, font = ('helvetica', 12, 'bold'), textvariable = input_text2, borderwidth=2) 
canvas1.create_window(550, 90, window=entry3)

label5 = tk.Label(root, text='Petal width :')
label5.config(font=('helvetica', 12),bg="violet",fg="black")
canvas1.create_window(400, 130, window=label5)

entry4 = tk.Entry (root, font = ('helvetica', 12, 'bold'), textvariable = input_text3, borderwidth=2) 
canvas1.create_window(550, 130, window=entry4)
 
label6 = tk.Label(root, text= 'Predicted Flower type is: ' ,font=('helvetica', 13),bg="violet",fg="black")
canvas1.create_window(230, 250, window=label6)

entry5 = tk.Entry (root, font = ('helvetica', 12, 'bold'), textvariable = result, borderwidth=2) 
canvas1.create_window(430, 250, window=entry5)

w = tk.Label(root, text="Don't Forget to Import Dataset Before Clicking Predict", bg="red", fg="yellow")
w.pack(fill=tk.X)


def btnclear():
    input_text.set("")
    input_text1.set("")
    input_text2.set("")
    input_text3.set("")
    result.set("")

def getCSV ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    df = pd.read_csv (import_file_path, names=names)
    print (df)

def getPredict ():
    
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    x4 = entry4.get()
    list1=[x1,x2,x3,x4]
    
    array = df.values
    X = array[:, 0:4]
    Y = array[:, 4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,random_state=seed)
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    X1=[list1]
    predictions = knn.predict(X1)
    result.set(predictions)


csvButton = tk.Button(text="   CSV File   ", command=getCSV,activeforeground='blue', activebackground='pink',  font=('Times', 14),borderwidth=3,bg='#0052cc', fg='#ffffff')
canvas1.create_window(230, 190, window=csvButton)
   
predictButton = tk.Button(text="   Predict Iris Flower   ", command=getPredict, activebackground='pink', activeforeground='blue', font=('Times', 14), borderwidth=3,bg='#0052cc', fg='#ffffff')
canvas1.create_window(470, 190, window=predictButton)

 
root.mainloop()