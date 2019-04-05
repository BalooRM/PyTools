#!/perl
use strict;
 
my $i;
my %wordhash;
 
while (my $text = <STDIN>) {
    chomp ($text);
    if($text !~ m/^\#/g) {
	$text = lc($text);
	$text =~ s/\./ /g;
	$text =~ s/\;/ /g;
	$text =~ s/\:/ /g;
	$text =~ s/\!/ /g;
	$text =~ s/\?/ /g;
	$text =~ s/\,/ /g;
	$text =~ s/\// /g;
	$text =~ s/(\'s|\’s)/ /g;
	$text =~ s/\"/ /g;
	$text =~ s/(\”|\“)/ /g;
	$text =~ s/(\(|\))/ /g;
	$text =~ s/^\s+//;  # trim left whitespace
	$text =~ s/\s+$//;  # trim right whitespace
	#       my @field = split / /, $text;
	my @field = split /\s+/, $text;
	#print "$text\n";
	#print @field.":\t";
	for ($i=0; $i<@field; ++$i) {
	    #    print "$field[$i]\t";
	    $field[$i] = ucfirst($field[$i]);
	    if (!defined ($wordhash{$field[$i]})) {
		$wordhash{$field[$i]} = 1;
	    } else {
		$wordhash{$field[$i]} += 1;
	    }
	}
	#print "\n";
    }
}

#print "\n";

#foreach my $k (sort keys %wordhash) {
foreach my $k (sort {$wordhash{$b} <=> $wordhash{$a}} sort keys %wordhash) {
    if ($k !~ m/(^And$|^Or$|^The$|^To$|^Of$|^In$|^A$|^Is$|^For$|^I$|^Are$|^Our$|^That$|^We$|^As$|^With$|^Be$|^This$|^Have$|^At$|^Has$|^It$|^Not$|^Who$|^Can$|^Don\'t$|^On$|^They$|^\-$|^An$|^There$|^Through$|^What$|^Am$|^Each$|^If$|^There$|^\-*\-$|^S$|^By$|^B$|^E$)/) {
print $k . "\t" . $wordhash{$k} ."\n";
    }
}
