#!/usr/bin/env ruby
print ARGV[0].scan(/from:(\+?[0-9]{10}|[a-zA-Z]+)/).join
print(",")
print ARGV[0].scan(/to:(\+?[0-9]{10}|[a-zA-Z]+)/).join
print(",")
print ARGV[0].scan(/\-?[0-9]\:\-?[0-9]\:\-?[0-9]\:\-?[0-9]\:\-?[0-9]/).join
print("\n")
