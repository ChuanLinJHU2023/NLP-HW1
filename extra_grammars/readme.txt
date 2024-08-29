From: Jason Eisner <jason@cs.jhu.edu>
To: Eric Goldlust
Cc: cs465 at cs dot jhu dot edu
Subject: Re: different grammar file

Eric Goldlust writes:

> I finished my random sentence generator and I was wondering about
> something.  Is there anywhere I can get a larger grammar?  This program
> is fun to play with and a larger grammar would make it somewhat less
> repetitive.  Do you know of a several-megabyte (or something) grammar?

Anyone writing such a big grammar of English would want to use a
somewhat more flexible format.  The simple format we are using for the
assignment is a little cumbersome in practice.  You may start to see
why later in the assignment.

Nonetheless, just for fun, I am glad to supply two extra grammars 
for you to play with.  You can find them at
  http://cs.jhu.edu/~jason/465/hw1/extra-grammars/

holygrail - also a very simple grammar, but it has a bigger
  vocabulary.  You might enjoy trying to improve it.  The vocabulary
  comes from the opening scene of Monty Python and the Holy Grail.

wallstreet - a large grammar that can generate all the sentences in 
  a one-million-word sample of the Wall Street Journal.  Unfortunately,
  it can also generate ungrammatical sentences, and mostly does so.
  THE GRAMMARS THAT *YOU* WRITE FOR THIS HOMEWORK ARE *NOT* SUPPOSED
  TO GENERATE ANY UNGRAMMATICAL SENTENCES.  But it's fun to try
  your randsent program on the wallstreet grammar anyway!(*)

Later in the course, you'll see where the wallstreet grammar came from
and why it might be useful.

-cheers, jme

(*)I tried running mine and it opined: "Mr. Bush be Corp."  Perhaps
that is the distilled essence of the Wall Street Journal?
