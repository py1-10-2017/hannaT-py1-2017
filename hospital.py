class Patient(object):
    bed_number = 0
    id = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        Patient.id += 1
        Patient.bed_number +=1
        self.id = Patient.id
        self.bed_number = Patient.bed_number
    def show_patient(self):
        print self.name
        print self.allergies
        print "Id {}".format(self.id)
        print "Bed Number {}".format(self.bed_number)

patient1 = Patient("John Adams", "Latex")
patient1.show_patient()
patient2 = Patient("Jane Johnson", "food")
patient2.show_patient()
patient3 = Patient("Jo Michaels", "Latex")
patient3.show_patient()



class Hospital(object):
    def __init__(self, hospital_name, capacity, patients=[]):
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.patients = patients
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Cannot add more patients becasue hospital is full"
            return self
        else:
            self.patients.append(patient)
            return self
    def discharge(self, patient):
        for p in self.patients:
            if p == patient:
                patient.bed_number = 0
                self.patients.remove(patient)
                print "patient {}".format(p.name) +' has been discharged'
                return self
    
    def show_hospital_info(self):
        print self.hospital_name
        print "capacity is {}".format(self.capacity)
        print 'The following patients are active'
        for p in self.patients:
            print "patient ID {}".format(p.id) 
            print "patient's Name {}".format(p.name)


hospital1 = Hospital('north side', 3)
hospital1.admit(patient1).admit(patient2).admit(patient3).discharge(patient1).show_hospital_info()