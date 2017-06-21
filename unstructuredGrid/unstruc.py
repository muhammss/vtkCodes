import vtk
import numpy as numpy
import glob
import vtk.util.numpy_support as vtkNP

class vtkFileRead():
	
	def __init__(self):
		self.filename = '1.vtk'

	def setFile(self,Fname):
		self.filename = Fname

	def readFile():
		self.reader = vtk.vtkUnstructuredGridReader()
		try:
			self.reader.SetFilename(self.filename)
		except:
			if len(self.filename)<=0:
				print ('Filename not set')
				return
			else:
				print ('Could not find file:', self.filename)
				return

		self.reader.ReadAllFieldsOn()
		self.reader.ReadAllScalarsOn()
		self.reader.ReadAllTensorsOn()
		self.reader.ReadAllNormalsOn()
		self.reader.ReadAllVectorsOn()
		self.reader.ReadAllColorScalarsOn()
		self.reader.ReadAllTCoordsOn()
		self.reader.Update()
		return self.reader

	def getReaderOutput(self):
		self.readerOutput = self.reader.GetOutput()
		return self.readerOutput

	def getCellData(self):
		self.output = self.reader.GetOutput()
		self.cellData = self.output.getCellData()
		return self.cellData

	def getVariableNames(self):
		VarNames = []
		for i in range(0,self.cellData.GetNumberOfArrays()-1):
			varNames.append(self.cellData.GetArrayName(i))
		return VarNames

	