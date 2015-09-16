#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docfly.member import Package, Module
import os

class DocflyError(Exception):
    pass

class Docfly():
    def __init__(self, package_name, dst="_source"):
        self.package = Package(package_name)
        self.dst = dst
        
    def fly(self):
        dst = self.dst
        
        try:
            os.mkdir(dst)
        except:
            pass

        for path in os.listdir(os.path.abspath(dst)):
            try:
                os.remove(path)
            except:
                pass
            
        # === start ===                  
        for package, full_name, packages, modules in self.package.walk():
            dir_path = os.path.join( *(
                    [dst, ] + full_name.split(".")
                    ) )
            init_path = os.path.join(dir_path, "__init__.rst")
            self.make_dir(dir_path)
            self.make_file(init_path, self.package_content(package))
            
            for module in modules:
                module_path = os.path.join(dir_path, module.name + ".rst")
                self.make_file(module_path, self.module_content(module))
        
    
    def make_dir(self, abspath):
        try:
            os.mkdir(abspath)
            print("made %s" % abspath)
        except:
            pass
    
    def make_file(self, abspath, text):
        try:
            with open(abspath, "w") as f:
                f.write(text)
            print("made %s" % abspath)
        except:
            pass
        
    def package_content(self, package):
        if isinstance(package, Package):
            header = "%s\n%s" % (package.name, "=" * len(package.name))
            automodule = "\n\n.. automodule:: %s\n\t:members:" % package.fullname
            header2 = "\n\nsubpackage and modules\n----------------------"
            toctree = "\n\n.. toctree::\n   :maxdepth: 1\n\n"
            
            lines = list()
            for p in package.subpackage.values():
                lines.append("\t%s <%s>" % (p.name, p.name + "/__init__"))
            for m in package.module.values():
                lines.append("\t%s <%s>" % (m.name, m.name))
                
            content = "{0}{1}{2}{3}{4}".format(
                header, 
                automodule, 
                header2, 
                toctree, 
                "\n".join(lines))

            return content
        else:
            raise Exception("%s is not a Package object" % repr(package))
    
    def module_content(self, module):
        if isinstance(module, Module):
            header = "%s\n%s" % (module.name, "=" * len(module.name))
            automodule = "\n\n.. automodule:: %s\n\t:members:" % module.fullname
            content = "{0}{1}".format(header, automodule)
            return content
        else:
            raise Exception("%s is not a Module object" % repr(module))
    
if __name__ == "__main__":
    docfly = Docfly("toppackage")
    docfly.fly()
    