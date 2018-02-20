#!/usr/bin/env ruby
print ARGV[0].scan(/from:(\+?[0-9]+|[a-zA-Z]+)/).join
print(",")
print ARGV[0].scan(/to:(\+?[0-9]+|[a-zA-Z]+)/).join
print(",")
print ARGV[0].scan(/flags:(\-?[0-9]\:\-?[0-9]\:\-?[0-9]\:\-?[0-9]\:\-?[0-9])/).join
print("\n")
