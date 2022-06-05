from abc import abstractmethod
from abc import ABCMeta

class Funcdecl(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass


class FuncdeclConcrete(Funcdecl):
  def __init__(self, signature, body):
    self.signature = signature
    self.body = body
  def accept(self, visitor):
    return visitor.visitfuncdeclconcrete(self)


class Signature(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass


class SignatureConcrete(Signature):
    def __init__(self, name, sigparams):
      self.name = name
      self.sigparams = sigparams
    def accept(self, visitor):
      return visitor.visitsignatureconcrete(self)


class Sigparams(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass


class SigparamsSingleConcrete(Sigparams):
  def __init__(self, var):
    self.var = var
  def accept(self, visitor):
    return visitor.visitsigparamssingleconcrete(self)

    
class SigparamsMultiConcrete(Sigparams):
  def __init__(self, var, sigParams):
    self.var = var
    self.sigParams = sigParams
  def accept(self, visitor):
    return visitor.visitsigparamsmulticoncrete(self)

class Body(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class BodyConcrete(Body):
  def __init__(self, stms):
    self.stms = stms
  def accept(self, visitor):
    return visitor.visitbodyconcrete(self)

class Stms(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmsSingleConcrete(Stms):
  def __init__(self, stm):
    self.stm = stm
  def accept(self, visitor):
    return visitor.visitstmssingleconcrete(self)

class StmsMultiConcrete(Stms):
  def __init__(self, stm, stms):
    self.stm = stm
    self.stms = stms
  def accept(self, visitor):
    return visitor.visitstmsmulticoncrete(self)
##
class Stm(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmConcrete(Stm):
  def __init__(self, exp):
    self.exp = exp
  def accept(self, visitor):
    return visitor.visitstmconcrete(self)


class Call(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpCallSingleConcrete(Call):
  def __init__(self, namefunc):
    self.namefunc = namefunc
  def accept(self, visitor):
    return visitor.visitexpcallsingleconcrete(self)

##adicionei aqui

class While(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class StmWhileConcrete(While):
  def __init__(self, exp, body):
    self.exp = exp
    self.body = body
  def accept(self, visitor):
    return visitor.visitstmwhileconcrete(self)



class For(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmForConcrete(For):
  def __init__(self,nameobj,namelist,body):
    self.nameobj = nameobj
    self.namelist = namelist
    self.body = body
    
  def accept(self,visitor):
    return visitor.visitstmforconcrete(self)



class If(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass
    
class SIFConcrete(If):
  def __init__(self, exp, s1 , s2):
    self.exp = exp
    self.s1 = s1
    self.s2 = s2

  def accept(self, visitor):
    return visitor.visitsifconcrete(self)

class Exp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpPlusConcrete(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpgeralconcrete(self)

class ExpMinusConcrete(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpgeralconcrete(self)

class ExpTimesConcrete(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2
  def accept(self, visitor):
    return visitor.visitexpgeralconcrete(self)

class Bodyclass(metaclass = ABCMeta):
  @abstractmethod
  
  def accept(self, visitor):
    pass


class BodyclassConcrete(bodyclassobj):
  def __init__(self,decl,bodyclass):
    self.decl = decl
    sefl.bodyclass = bodyclass
  def accept(self, visitor):
    return visitor.visitbodyclassconcrete(self)

class Attdecl(metaclass = ABCMeta):
  @abstractmethod
  
  def accept(self, visitor):
    pass


class AttdeclConcrete(Attdecl):
  def __init__(self, var , objdecl)
    self.var = var
    self.objdecl = objdecl

  def accept(self):
    return visitor.visitattdeclconcrete(self)



class Objdecl(metaclass = ABCMeta):
  @abstractmethod
  
  def accept(self, visitor):
    pass


class ObjdeclConcrete(Objdecl):
  def __init__(self, var1, var2)
    self.var1 = var1
    self.var2 = var2

  def accept(self):
    return visitor.visitobjdeclconcrete(self)



class Callobj(metaclass = ABCMeta):
  @abstractmethod
  
  def accept(self, visitor):
    pass


class CallobjConcrete(Callobj):
  def __init__(self, var1, var2)
    self.var1 = var1
    self.var2 = var2

  def accept(self):
    return visitor.visitcallobjconcrete(self)

class Assign(metaclass = ABCMeta):
  @abstractmethod

  def accept(self,visitor):
    pass

class AssignConcrete(assign):
  def __init__(self, var, exp)
    self.var = var
    self.exp = exp

  def accept(self):
    return visitor.visitassignconcrete(self)

class Params(metaclass = ABCMeta):
  @abstractmethod

  def accept(self, visitor):
    pass

class ParamssingleConcrete(self, params):
  def __init__(self, exp)
    self.exp = exp

  def accept(self):
    return visitor.visitparamssingleconcrete(self)
  
  
  