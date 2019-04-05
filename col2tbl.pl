#!/perl
use strict;
my $i = 0;
 
while (my $text = <STDIN>) {
    chomp ($text);
    print "$text";
    if(++$i >= 10) {
	print "\n";
	$i = 0;
    }
}

