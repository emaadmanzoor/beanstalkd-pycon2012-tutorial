# Building A Cluster with Beanstalkd

*A PyCon 2012 Tutorial*

The Pycon India 2012 funnel has all the [tutorial details](http://in.pycon.org/2012/funnel/pyconindia2012/55-simple-linux-cluster-with-python-and-beanstalkd).

## Speakers

   * [@racheesingh](https://github.com/racheesingh/), working at Arista Networks.
   * [@emaadmanzoor](https://github.com/emaadmanzoor), working at Yahoo!.

We'd worked on this as a [course project](https://github.com/emaadmanzoor/distributed-pi-estimation)
under the guidance of [Dr. Biju K. Raveendran](http://www.bits-pilani.ac.in/goa/biju/Profile) at BITS - Pilani, Goa Campus.

## Slides

We decided to build a terminal presentation, since we'd be spending most of
our time with code in the terminal. This was possible with the very awesome
[tkn](https://github.com/fxn/tkn) by [@fxn](https://github.com/fxn).

We compiled the terminal snapshots into a [presentation on SpeakerDeck](https://speakerdeck.com/u/emaadmanzoor/p/building-a-cluster-with-python-and-beanstalkd).

### Viewing In The Terminal

To view the slides, first set up Ruby and [tkn](https://github.com/fxn/tkn) as described
in the repository documentation.

Then you'll need to enable the RailsCasts Pygments style we use; to do that,
drop in `__init__.py` and `railscasts.py` into the `pygments` styles
directory created by the `pygments.rb` gem. For me on OSX Lion, this was:
`~/.rvm/gems/ruby-1.9.3-p194/gems/pygments.rb-0.2.13/vendor/pygments-main/pygments/styles/`

Run the presentation in the terminal by executing the Ruby script in the `presentation` directory:
`bundle exec bin/tkn beanstalkd-pycon2012.rb`

## Contact

   * emaadmanzoor@gmail.com
   * rachee.singh@gmail.com
