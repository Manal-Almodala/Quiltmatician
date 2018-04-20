import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

class Square():
	def __init__(self,size,color):
		self.size = size
		self.color = color

class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initGUI()
        self.parent.configure(background='#031424')
        self.initBitMap()
        self.paintGrid()

    def on_configure(self,event):
        self.gridCanvas.configure(scrollregion=self.gridCanvas.bbox('all'))

    def initGUI(self):

    	self.parent.title("Quiltmatician")
    	self.parent.geometry("776x710")
    	self.parent.resizable(width=False,height=False)

    	self.gridLength = 360 #10 yards
    	self.gridWidth = 84
    	
    	''' Maybe add photo background in future:
    	image = Image.open("//Users/brentbadhwar/Desktop/balt8.gif")
    	photo = ImageTk.PhotoImage(image)
    	label = tk.Label(image=photo)
    	label.image = photo # keep a reference!
    	label.place(x=220,y=0)  
    	'''

    	title = tk.Label(self.parent,text="Quiltmatician",font="Helvetica",foreground='white')
    	title.place(x=270,y=1)
    	title.configure(background='#031424')
    	titleFont = Font(family="American Typewriter",size=35)
    	title.configure(font=titleFont)

    	self.inputCanvas = tk.Canvas(self.parent,width=752,height=215,background='#30415D',highlightthickness=1.6)
    	self.inputCanvas.place(x=10,y=470)

    	tk.Label(self.parent,text="Enter number of 2 1/2 inch squares: ",foreground='white',background='#30415D',font=Font(family="American Typewriter",size=20)).place(x=20,y=480)
    	tk.Label(self.parent,text="Enter number of 3 1/2 inch squares: ",foreground='white',background='#30415D',font=Font(family="American Typewriter",size=20)).place(x=20,y=510)
    	tk.Label(self.parent,text="Enter number of 4 1/2 inch squares: ",foreground='white',background='#30415D',font=Font(family="American Typewriter",size=20)).place(x=20,y=540)
    	tk.Label(self.parent,text="Enter number of 6 1/2 inch squares: ",foreground='white',background='#30415D',font=Font(family="American Typewriter",size=20)).place(x=20,y=570)
    	tk.Label(self.parent,text="Enter number of 9 1/2 inch squares: ",foreground='white',background='#30415D',font=Font(family="American Typewriter",size=20)).place(x=20,y=600)
        
    	self.TwoHalfEntry = tk.Entry(self.parent,width=3,foreground='black',highlightbackground='#30415D')
    	self.TwoHalfEntry.insert(0,"0")
    	self.TwoHalfEntry.place(x=370,y=480)
    	self.ThreeHalfEntry = tk.Entry(self.parent,width=3,foreground='black',highlightbackground='#30415D')
    	self.ThreeHalfEntry.insert(0,"0")
    	self.ThreeHalfEntry.place(x=370,y=510)
    	self.FourHalfEntry = tk.Entry(self.parent,width=3,foreground='black',highlightbackground='#30415D')
    	self.FourHalfEntry.insert(0,"0")
    	self.FourHalfEntry.place(x=370,y=540)
    	self.SixHalfEntry = tk.Entry(self.parent,width=3,foreground='black',highlightbackground='#30415D')
    	self.SixHalfEntry.insert(0,"0")
    	self.SixHalfEntry.place(x=370,y=570)
    	self.NineHalfEntry = tk.Entry(self.parent,width=3,foreground='black',highlightbackground='#30415D')
    	self.NineHalfEntry.insert(0,"0")
    	self.NineHalfEntry.place(x=370,y=600)

    	tk.Label(self.parent,text="You will need... ",foreground='white',background='#30415D',font=Font(family="American Typewriter",size=25)).place(x=500,y=510)
    	self.neededLengthLabel = tk.Label(self.parent,foreground='white',background='#30415D',font=Font(family="American Typewriter",size=25))
    	self.neededLengthLabel.place(x=515,y=570)

    	self.CalculateButton = tk.Button(self.parent,text="Calculate",command=self.calculate,height=2,width=10,foreground='grey25',background= 'grey25',highlightcolor='grey25',highlightthickness=0,font=("Helvetica",13,"bold"))
    	self.CalculateButton.place(x=120,y=645)

    	self.ClearButton = tk.Button(self.parent,text="Reset",command=self.clear,height=2,width=10,foreground='grey25',background='grey25',highlightthickness=0,font=("Helvetica",13,"normal"))
    	self.ClearButton.place(x=220,y=645)

    	self.gridCanvas = tk.Canvas(self.parent,width=750,height=400,background='#8EAEBD',highlightbackground='white',highlightthickness=2.5)
    	self.scrollbar = tk.Scrollbar(self.parent, command=self.gridCanvas.yview)
    	self.scrollbar.pack(side=tk.RIGHT, fill='y')
    	self.scrollbar.place(x=753,y=52,width=13,height=404)
    	self.gridCanvas.pack(side=tk.RIGHT)
    	self.gridCanvas.place(x=10,y=50) 
    	self.gridCanvas.configure(yscrollcommand = self.scrollbar.set)

    	self.placeLengthMarkings()

    	self.gridCanvas.bind('<Configure>', self.on_configure)

    	self.frame = tk.Frame(self.gridCanvas)
    	self.gridCanvas.create_window((0,0), window=self.frame, anchor='nw')

    def initBitMap(self): 
    	self.bitMap = [[0.0]*self.gridWidth for _ in range(self.gridLength)]

    def clearBitMap(self):
    	for i in range(self.gridLength):
    		for j in range (self.gridWidth):
    			self.bitMap[i][j] = 0.0

    def placeLengthMarkings(self):
    	lengthMarkString = "0"
    	posY = 33
    	for i in range(int(self.gridLength//9+1)):
    		self.gridCanvas.create_text(16,posY,text=lengthMarkString,font=("American Typewriter",13,"normal"),fill='white')
    		lengthMarkString = str(float(lengthMarkString) + .125)   		
    		posY += 72

    def paintGrid(self):
        canvasX = 35
        canvasY = 33
        for i in range(self.gridLength):
            for j in range(self.gridWidth):
                self.gridCanvas.create_rectangle(canvasX,canvasY,canvasX+8,canvasY+8,fill='grey90')
                canvasX += 8
            canvasX = 35
            canvasY += 8

    def addShapeToBitMap(self,x,y,shape):
        xUpper = x+int(shape.size*2)
        yUpper = y+int(shape.size*2)
        for i in range(y,yUpper):
            for j in range(x,xUpper):
                self.bitMap[i][j] = shape.size

    def spotIsFree(self,x,y,shape):
        xUpper = x+int(shape.size*2)
        yUpper = y+int(shape.size*2)
        if (xUpper > self.gridWidth):
        	return False
        for i in range(y,yUpper):
            for j in range(x,xUpper):
                if (self.bitMap[i][j] > 0):
                    return False
        return True

    def clearShape(self,curX,curY,dim):
        for i in range(curY,int(curY+dim)):
            for j in range(curX,int(curX+dim)):
                self.bitMap[i][j] = 0

    def getLengthNeeded(self):
    	maxLength = 0
    	for i in range(self.gridWidth):
    	    j = 0
    	    while (self.bitMap[j][i] != 0 and j < self.gridWidth):
    	    	j += 1
    	    if (j > maxLength):
    	    	maxLength = j
    	return maxLength/72


    def fillGrid(self,squareList):
        curX = 0
        curY = 0

        while (squareList):
            currentShape = squareList[0]
            squareList.pop(0)
            currentShapeHasBeenAdded = False
            curX = 0
            curY = 0
            while (curY < self.gridLength and not(currentShapeHasBeenAdded)):
                while(curX < self.gridWidth-currentShape.size and not(currentShapeHasBeenAdded)):
                    if (self.spotIsFree(curX,curY,currentShape)):
                        self.addShapeToBitMap(curX,curY,currentShape)
                        curX += currentShape.size*2
                        currentShapeHasBeenAdded = True
                    else:
                        curX += 1
                curX = 0
                curY += 1
            
    def paintShapes(self):
        shapeColor = {2.5 : "#ffb3ba", 3.5 : "#ffdfba", 4.5 : "#ffffba", 6.5 : "#baffc9", 9.5 : "#b19cd9"}
        currentShapeDim = 0
        canvasX = 35
        canvasY = 33
        for i in range(self.gridLength):
            for j in range(self.gridWidth):
                currentShapeDim = self.bitMap[i][j]
                if (currentShapeDim > 0):
                    fillColor = shapeColor[self.bitMap[i][j]]
                    self.gridCanvas.create_rectangle(canvasX,canvasY,canvasX+8*currentShapeDim*2,canvasY+8*currentShapeDim*2,fill=fillColor,width=2,tag="shape")
                    self.clearShape(j,i,currentShapeDim*2)
                    self.paintShapeGridLines(canvasX,canvasY,currentShapeDim*2,fillColor)                    	
                canvasX += 8
            canvasX = 35
            canvasY += 8

    def printShapeSizeLabels(self,curX,curY,dim):
        self.gridCanvas.create_text(canvasX+40,canvasY+40,text="9 1/2",font=("American Typewriter",16,"normal"))

    def paintShapeGridLines(self,curX,curY,dim,color):
        for i in range(int(dim)):
            for j in range(int(dim)):
                     self.gridCanvas.create_rectangle(curX+8*j,curY+8*i,curX+8*(j+1),curY+8*(i+1),fill=color,tag="shape")
        self.gridCanvas.create_line(curX,curY,curX+8*dim,curY,width=2,tag="shape")
        self.gridCanvas.create_line(curX,curY,curX,curY+8*dim,width=2,tag="shape") 
        self.gridCanvas.create_line(curX,curY+8*dim,curX+8*dim,curY+8*dim,width=2,tag="shape") 
        self.gridCanvas.create_line(curX+8*dim,curY,curX+8*dim,curY+8*dim,width=2,tag="shape")  

    def clear(self):
    	self.gridCanvas.delete("shape")

    	self.TwoHalfEntry.delete(0,"end")
    	self.TwoHalfEntry.insert(0,"0")
    	self.ThreeHalfEntry.delete(0,"end")
    	self.ThreeHalfEntry.insert(0,"0") 
    	self.FourHalfEntry.delete(0,"end")
    	self.FourHalfEntry.insert(0,"0")
    	self.SixHalfEntry.delete(0,"end")
    	self.SixHalfEntry.insert(0,"0")             	
    	self.NineHalfEntry.delete(0,"end")
    	self.NineHalfEntry.insert(0,"0") 

    def calculate(self):

        self.gridCanvas.delete("shape")
        
        if (not isinstance(int(self.NineHalfEntry.get()), int) or int(self.NineHalfEntry.get()) < 0):
            self.NineHalfEntry.delete(0,"end")
            self.NineHalfEntry.insert(0,"0")
        if (not isinstance(int(self.SixHalfEntry.get()), int) or int(self.SixHalfEntry.get()) < 0):
            self.SixHalfEntry.delete(0,"end")
            self.SixHalfEntry.insert(0,"0")
        if (not isinstance(int(self.FourHalfEntry.get()), int) or int(self.FourHalfEntry.get()) < 0):
            self.FourHalfEntry.delete(0,"end")
            self.FourHalfEntry.insert(0,"0")
        if (not isinstance(int(self.ThreeHalfEntry.get()), int) or int(self.ThreeHalfEntry.get()) < 0):
            self.ThreeHalfEntry.delete(0,"end")
            self.ThreeHalfEntry.insert(0,"0")
        if (not isinstance(int(self.TwoHalfEntry.get()), int) or int(self.TwoHalfEntry.get()) < 0):
            self.TwoHalfEntry.delete(0,"end")
            self.TwoHalfEntry.insert(0,"0")

        self.squareList = []
        for i in range(int(self.NineHalfEntry.get())):
            self.squareList.append(Square(9.5,"red"))
        for i in range(int(self.SixHalfEntry.get())):
            self.squareList.append(Square(6.5,"blue"))
        for i in range(int(self.FourHalfEntry.get())):
            self.squareList.append(Square(4.5,"green"))
        for i in range(int(self.ThreeHalfEntry.get())):
            self.squareList.append(Square(3.5,"yellow"))
        for i in range(int(self.TwoHalfEntry.get())):
            self.squareList.append(Square(2.5,"orange"))

        tempSquareList = self.squareList.copy()
        self.initBitMap() 
        self.fillGrid(tempSquareList)
        self.lengthNeeded = self.getLengthNeeded()
        self.neededLengthLabel.config(text=str( round(self.lengthNeeded,3)) + " yards")
        self.paintGrid()
        self.paintShapes()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)#.pack(side="top", fill="both", expand=True)
    root.mainloop()