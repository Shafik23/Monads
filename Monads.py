'''
I will attempt to use Python as a way to introduce Monads to the
imperative programmer.

Here are some key points:

1. Monads are generally not useful for languages that allow side-effects and
state in functions - hence the lack of monads in langauges like C/C++/Java.
It might be cleaner in certain scenarios to use a monad-like pattern in C++, but it's never
necessary. Contrast that with languages like Haskell, where you *have* to use a monad to do
IO, for example.

2. You should think of monads as a *general design pattern* for composing functions in useful
ways. Examples of "useful" patterns for monads include: exception handling, concurrency, searching, etc.
Note that "function" here refers to pure functions, which are strict mappings from one set to
another, with no side effects.

3. Languages like Haskell make the Monad pattern "feel natural" in the language's syntax.

4. The Monad pattern makes heavy use of the fact that functions are "first class citizens", and
can be passed in to other functions, returned from functions, etc. Think partial application, currying, etc.

5. The "bind" function of a Monad is where the magic happens: it defines the behavior of how other
functions are chained together.

'''


class SimpleMonad:
   '''
   This is the simplest implementation of a "monad". "f" is a function that
   itself returns a monad.
   '''
   def __init__(self, val):
      self.val = val

   def bind(self, f):
      return f(self.val)


class MaybeMonad(SimpleMonad):
   '''
   This is usually the first real-life example of a monad that you'll come across.
   It's a monad (i.e. function-composition-pattern) for cleanly dealing with errors.
   This is sometimes also called an "Exception Monad".
   '''
   def __init__(self, val):
      self.val = val

   def bind(self, f):
      if self.val is None:
         return self
      else:
         return f(self.val)


def square(x):
   return MaybeMonad(x**2)

def doubler(x):
   return MaybeMonad(x*2)

def sqrt(x):
   if x < 0:
      return MaybeMonad(None)

   return MaybeMonad(x**0.5)


###
# Entry point
###
if __name__ == '__main__':
   sm = SimpleMonad(3).bind(square).bind(doubler)
   print(sm.val)

   mm = MaybeMonad(4).bind(square).bind(doubler)
   print(mm.val)

   mm = MaybeMonad(5).bind(square).bind(sqrt)
   print(mm.val)

   # note how no exception is thrown in the following line:
   # the returned value is simply 'None'
   mm = MaybeMonad(-3).bind(sqrt).bind(doubler).bind(doubler)
   print(mm.val)
