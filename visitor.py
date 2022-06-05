from abstract_visitor import *
#from src.semantic.SymbolTable import Types
# global tab
tab = 0

class Visitor(AbstractVisitor):
  def visitfuncdeclconcrete(self,funcdecl):
    funcdecl.signature.accept(self)
    funcdecl.body.accept(self)

    
  def visitsignatureconcrete(self,signature):
    print(signature.name,end = ' ')
    signature.sigparams.accept(self)

  
  def visitsigparamssingleconcrete(self,sigparams):
    print(sigparams.var)

    
  def visitsigparamsmulticoncrete(self,sigparams):
    print(sigparams.var, ", " , end = ' ')
    sigparams.sigParams.accept(self)

  def visitbodyconcrete(self, body):
    body.stms.accept(self)
    print()
    print("end")

  def visitstmssingleconcrete(self, stms):
    stms.stm.accept(self)

  def visitstmsmulticoncrete(self, stms):
    stms.stm.accept(self)
    stms.stms.accept(self)

  def visitstmconcrete(self, stm):
    stm.exp.accept(self)

  #def visitexpconcrete(self, exp):

  def visitexpcallsingleconcrete(self, call):
    print()
    print(call.namefunc,'()')

#comecei aqui
  def visitstmwhileconcrete(self, whileobj):
    whileobj.exp.accept(self)
    whileobj.body.accept(self)
    print()
    print("while")

  def visitstmforconcrete(self, forobj):
    print(forobj.nameobj, end = ' ')
    print(forobj.namelist, end = ' ')
    forobj.body.accept(self)
    print()
    print("for")

  def visitsifconcrete(self, ifobj):
    ifobj.exp.accept(self)
    ifobj.s1.accept(self)
    if ifobj.s2 != None:
      ifobj.s12.accept(self)

  #def expplusconcrete(self, exp):
  #  exp.exp1.accept(self)
  #  exp.exp2.accept(self)

  #def expminusconcrete(self, exp):
  #  exp.exp1.accept(self)
  #  exp.exp2.accept(self)
  
  def visitexpgeralconcrete(self, exp):
    exp.exp1.accept(self)
    exp.exp2.accept(self)

  def visitbodyclassconcrete(self, bodyclassobj):
    bodyclassobj.decl.accept(self)
    bodyclassobj.bodyclass.accept(self)

  def visitattdeclconcrete(self, attdecl):
    print( attdecl.var, end = ' ')
    attdecl.objdecl.accept(self)

  def visitcallobjconcrete(self, callobj):
    print( callobj.var1, end = ' ')
    print( callobj.var2, end = ' ')
    
    
  def visitassignconcrete(self, assign):
    print( assign.var, end = ' ')
    assign.exp.accept(self)

  def visitparamssingleconcrete(self, params):
    params.exp.accept(self)