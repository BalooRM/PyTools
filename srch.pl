#!\perl
use strict;
# R. Ballew, 14-Feb-2018
# Perform case-insensitive match one or more search terms to lines read 
# from STDIN
my $usage =
    "Usage: \n" .
    " > perl srch.pl first second < file.txt\n" . 
    " > perl srch.pl first second third < file.txt\n" .
    " > perl srch.pl \"first term\" second < file.txt\n";

#my $numARGV = $#ARGV;
#++$numARGV;
#if ($numARGV == 1) {
#    print "There is $numARGV command line argument.\n";
#} else {
#    print "There are $numARGV command line arguments.\n";
#}
#for (my $i = 0; $i <= $#ARGV; $i++) {
#    print "$ARGV[$i]\n";
#}

if ($#ARGV == -1) {
    print "$usage\n";
    die;
}

my $myMatchFlag;
my $myMatch; # assume match

# Read input data from STDIN. 
while (my $text = <STDIN>) {
    chomp ($text);
    $myMatch = 1;   # assume all terms match
    
    for (my $i = 0; $i <= $#ARGV; $i++) {
	if ($text =~ m/$ARGV[$i]/i) {
	    #print "$ARGV[$i] - $text\n";
	    $myMatchFlag = 1;
	} else {
	    $myMatchFlag = 0;
	}
	$myMatch = $myMatch * $myMatchFlag;
    }
    if ($myMatch == 1) {
	print "$text\n";
    }
}
