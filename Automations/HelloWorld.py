#type:ignore
from Icii import *

class HelloWorld(PythonAutomation): 
    def ApplyAutomation(self):
        
        if self.Items.Count > 0:
            name = self.Items.Get("name", 0)

            with self.CodeAfterAutomation: 
                print("Hello World! Welcome ((name)) to Arctic Fox")

        else:        
            with self.CodeAfterAutomation: 
                print("Howdy World!")