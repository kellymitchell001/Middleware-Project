import datetime

class Manufacturer():
    def __init__(self, name_, registered_country_, contact_person_):
        self.name = name_
        self.registered_country = registered_country_
        self.contact_person = contact_person_
    def getName(self):
        return self.name
    def setName(self, a):
        self.name = a
    def getRegCountry(self):
        return self.registered_country 
    def setRegCountry(self, a):
        self.registered_country = a
    def getContact(self):
        return self.contact_person 
    def setContact(self, a):
        self.contact_person = a

class User():
    def __init__(self, username_, password_, firstName_, middleName_, lastName_, companyName_, companyType_, address_, officePhone_, cellphone_, email_):
        self.username = username_
        self.password = password_
        self.firstName = firstName_
        self.middleName = middleName_
        self.lastName = lastName_
        self.address = address_
        self.companyName = companyName_
        self.companyType = companyType_
        self.officePhone = officePhone_
        self.cellphone = cellphone_
        self.email = email_
    def getUsername (self):
        return self.username 
    def setUsername (self, a):
        self.username = a
    def getPassword(self):
        return self.password
    def setPassword(self, a):
        self.password= a
    def getFirstName (self):
        return self.firstName 
    def setFirstName (self, a):
        self.firstName = a
    def getMiddleName (self):
        return self.middleName 
    def setMiddleName (self, a):
        self.middleName = a
    def getLastName (self):
        return self.lastName 
    def setLastName (self, a):
        self.lastName = a
    def getAddress (self):
        return self.address 
    def setAddress (self, a):
        self.address = a
    def getOfficePhone (self):
        return self.officePhone 
    def setOfficePhone (self, a):
        self.officePhone = a
    def getCellPhone (self):
        return self.cellPhone 
    def setCellPhone (self, a):
        self.cellPhone = a
    def getEmail (self):
        return self.email 
    def setEmail (self, a):
        self.email = a

class TestResults():
    def __init__(self, dataSource_, product_, reportingCondition_, testSquence_, testDate_, isc_, voc_, imp_, vmp_, pmp_, ff_, noct_):
        self.dataSource = dataSource_
        self.product = product_
        self.reportingCondition = reportingCondition_
        self.testSquence = testSquence_
        self.testDate = testDate_
        self.isc = isc_
        self.voc = voc_
        self.imp = imp_
        self.vmp = vmp_
        self.pmp = pmp_
        self.ff = ff_
        self.noct = noct_
    def getdataSource (self):
        return self.dataSource
    def setdataSource (self, a):
        self.dataSource = a
    def getproduct (self):
        return self.product 
    def setproduct (self, a):
        self.product = a
    def getreportingCondition (self):
        return self.reportingCondition 
    def setreportingCondition (self, a):
        self.reportingCondition = a
    def gettestSquence (self):
        return self.testSquence 
    def settestSquence (self, a):
        self.testSquence = a
    def gettestDate (self):
      return self.testDate 
    def settestDate (self, a):
        self.testDate = a
    def getisc (self):
        return self.isc 
    def setisc (self, a):
        self.isc = a
    def getvoc (self):
        return self.voc 
    def setvoc (self, a):
        self.voc = a
    def getimp (self):
        return self.imp 
    def setimp (self, a):
        self.imp = a
    def getvmp (self):
        return self.vmp 
    def setvmp (self, a):
        self.vmp = a
    def getpmp (self):
        return self.pmp 
    def setpmp (self, a):
        self.pmp = a
    def getff (self):
        return self.ff 
    def setff (self, a):
        self.ff = a
    def getnoct (self):
        return self.noct 
    def setnoct (self, a):
        self.noct = a

class TestLab():
    def __init__(self, name_, address_, contact_person_):
        self.name = name_
        self.address = address_
        self.contact_person = contact_person_
    def getname (self):
        return self.name
    def setname (self, a):
        self.name = a
    def getaddress (self):
        return self.address 
    def setaddress (self, a):
        self.address = a
    def getcontact_person (self):
        return self.contact_person 
    def setcontact_person (self, a):
        self.contact_person = a


class Product():
    def __init__(self, ModelNumber_, Manufacturer_, ManufacturingDate_, Length_, Width_, Weight_, CellArea_, CellTechnology_, TotalNumberOfCells_, NumberOfCellsInSeries_, NumberOfSeriesStrings_, NumberOfBypassDiodes_, SeriesFuseRating_, InterconnectMaterial_, InterconnectSupplier_, SuperstrateType_, SuperstrateManufacturer_, SubstrateType_, SubstrateManufacturer_, FrameMaterial_, FrameAdhesive_, EncapsulantType_, EncapsulantManufacturer_, JunctionBoxType_, JunctionBoxManufacturer_, JunctionBoxAdhesive_, CableType_, ConnectorType_, MaximumSystemVoltage_, RatedVoc_, RatedIsc_, RatedVmp_, RatedImp_, RatedPmp_, RatedFf_):
        self.ModelNumber = ModelNumber_
        self.Manufacturer = Manufacturer_
        self.ManufacturingDate = ManufacturingDate_
        self.Length = Length_
        self.Width = Width_
        self.Weight = Weight_
        self.CellArea = CellArea_
        self.CellTechnology = CellTechnology_
        self.TotalNumberOfCells = TotalNumberOfCells_
        self.NumberOfCellsInSeries = NumberOfCellsInSeries_
        self.NumberOfSeriesStrings = NumberOfSeriesStrings_
        self.NumberOfBypassDiodes = NumberOfBypassDiodes_
        self.SeriesFuseRating = SeriesFuseRating_
        self.InterconnectMaterial = InterconnectMaterial_
        self.InterconnectSupplier = InterconnectSupplier_
        self.SuperstrateType = SuperstrateType_
        self.SuperstrateManufacturer = SuperstrateManufacturer_
        self.SubstrateType = SubstrateType_
        self.SubstrateManufacturer = SubstrateManufacturer_
        self.FrameMaterial = FrameMaterial_
        self.FrameAdhesive = FrameAdhesive_
        self.EncapsulantType = EncapsulantType_
        self.EncapsulantManufacturer = EncapsulantManufacturer_
        self.JunctionBoxType = JunctionBoxType_
        self.JunctionBoxManufacturer = JunctionBoxManufacturer_
        self.JunctionBoxAdhesive = JunctionBoxAdhesive_
        self.CableType = CableType_
        self.ConnectorType = ConnectorType_
        self.MaximumSystemVoltage = MaximumSystemVoltage_
        self.RatedVoc = RatedVoc_
        self.RatedIsc = RatedIsc_
        self.RatedVmp = RatedVmp_
        self.RatedImp = RatedImp_
        self.RatedPmp = RatedPmp_
        self.RatedFf = RatedFf_
        
    def getModelNumber (self):
        return self.ModelNumber
    
    def setModelNumber (self, a):
        self.ModelNumber = a
        
    def getManufacturer (self):
        return self.Manufacturer
    
    def setManufacturer (self, a):
        self.Manufacturer = a
        
    def getManufacturingDate (self):
        return self.ManufacturingDate
    
    def setManufacturingDate (self, a):
        self.ManufacturingDate = a
    def getLength (self):
        return self.Length
    def setLength (self, a):
        self.Length = a
    def getWidth (self):
        return self.Width
    def setWidth (self, a):
        self.Width = a
    def getWeight (self):
        return self.Weight
    def setWeight (self, a):
        self.Weight = a
    def getCellArea (self):
        return self.CellArea
    def setCellArea (self, a):
        self.CellArea = a
    def getCellTechnology (self):
        return self.CellTechnology
    def setCellTechnology (self, a):
        self.CellTechnology = a
    def getTotalNumberOfCells (self):
        return self.TotalNumberOfCells
    def setTotalNumberOfCells (self, a):
        self.TotalNumberOfCells = a
    def getNumberOfCellsInSeries (self):
        return self.NumberOfCellsInSeries
    def setNumberOfCellsInSeries (self, a):
        self.NumberOfCellsInSeries = a
    def getNumberOfSeriesStrings (self):
        return self.NumberOfSeriesStrings
    def setNumberOfSeriesStrings (self, a):
        self.NumberOfSeriesStrings = a
    def getNumberOfBypassDiodes (self):
        return self.NumberOfBypassDiodes
    def setNumberOfBypassDiodes (self, a):
        self.NumberOfBypassDiodes = a
    def getSeriesFuseRating (self):
        return self.SeriesFuseRating
    def setSeriesFuseRating (self, a):
        self.SeriesFuseRating = a
    def getInterconnectMaterial (self):
        return self.InterconnectMaterial
    def setInterconnectMaterial (self, a):
        self.InterconnectMaterial = a
    def getInterconnectSupplier (self):
        return self.InterconnectSupplier
    def setInterconnectSupplier (self, a):
        self.InterconnectSupplier = a
    def getSuperstrateType (self):
        return self.SuperstrateType
    def setSuperstrateType (self, a):
        self.SuperstrateType = a
    def getSuperstrateManufacturer (self):
        return self.SuperstrateManufacturer
    def setSuperstrateManufacturer (self, a):
        self.SuperstrateManufacturer = a
    def getSubstrateType (self):
        return self.SubstrateType
    def setSubstrateType (self, a):
        self.SubstrateType = a
    def getSubstrateManufacturer (self):
        return self.SubstrateManufacturer
    def setSubstrateManufacturer (self, a):
        self.SubstrateManufacturer = a
    def getFrameMaterial (self):
        return self.FrameMaterial
    def setFrameMaterial (self, a):
        self.FrameMaterial = a
    def getFrameAdhesive (self):
        return self.FrameAdhesive
    def setFrameAdhesive (self, a):
        self.FrameAdhesive = a
    def getEncapsulantType (self):
        return self.EncapsulantType
    def setEncapsulantType (self, a):
        self.EncapsulantType = a
    def getEncapsulantManufacturer (self):
        return self.EncapsulantManufacturer
    def setEncapsulantManufacturer (self, a):
        self.EncapsulantManufacturer = a
    def getJunctionBoxType (self):
        return self.JunctionBoxType
    def setJunctionBoxType (self, a):
        self.JunctionBoxType = a
    def getJunctionBoxManufacturer (self):
        return self.JunctionBoxManufacturer
    def setJunctionBoxManufacturer (self, a):
        self.JunctionBoxManufacturer = a
    def getJunctionBoxAdhesive (self):
        return self.JunctionBoxAdhesive
    def setJunctionBoxAdhesive (self, a):
        self.JunctionBoxAdhesive = a
    def getCableType (self):
        return self.CableType
    def setCableType (self, a):
        self.CableType = a
    def getConnectorType (self):
        return self.ConnectorType
    def setConnectorType (self, a):
        self.ConnectorType = a
    def getMaximumSystemVoltage (self):
        return self.MaximumSystemVoltage
    def setMaximumSystemVoltage (self, a):
        self.MaximumSystemVoltage = a
    def getRatedVoc (self):
        return self.RatedVoc
    def setRatedVoc (self, a):
        self.RatedVoc = a
    def getRatedIsc (self):
        return self.RatedIsc
    def setRatedIsc (self, a):
        self.RatedIsc = a
    def getRatedVmp (self):
        return self.RatedVmp
    def setRatedVmp (self, a):
        self.RatedVmp = a
    def getRatedImp (self):
        return self.RatedImp
    def setRatedImp (self, a):
        self.RatedImp = a
    def getRatedPmp (self):
        return self.RatedPmp
    def setRatedPmp (self, a):
        self.RatedPmp = a
    def getRatedFf (self):
        return self.RatedFf
    def setRatedFf (self, a):
        self.RatedFf = a

def main():
    pass

if (__name__ == "__main__"):
    main()
