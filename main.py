#!/usr/bin/env python
import sys, argparse, logging

def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  
  # TODO Replace this with your actual code.
  
  logging.info("You passed an argument.")
  logging.debug("Your Argument: %s" % args.argument)

if __name__ == '__main__':
  parser = argparse.ArgumentParser( 
                                    description = "Does a thing to some stuff.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
  # TODO Specify your real parameters here.
  parser.add_argument(
                      "argument",
                      help = "pass ARG to the program",
                      metavar = "ARG")
  parser.add_argument(
                      "-v",
                      "--verbose",
                      help="increase output verbosity",
                      action="store_true")
  args = parser.parse_args()
  
  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO
  
  main(args, loglevel)