# Future work

## On mixins

Mixins are classes that contains methods for use by other classes without
having to be the parent class of those other classes. How those other classes
gain access to the mixin's methods depends on the language. Mixins are sometimes
described as being "included" rather than "inherited".

For this reason a common pattern with mixing is that they should not have a
constructor as this implies that an any class using a mixin now needs to make
sure that it follows some constructor which goes against the idea of just
injecting some functionality.

Some current examples on the Spyder code base that present this problem include:

* Mixing module!
