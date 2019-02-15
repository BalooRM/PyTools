package My::Stats;
use strict;
use warnings;

use Exporter qw(import);

our @EXPORT_OK = qw(Average Median Count Min Max Percentile);

=pod


=cut

sub Median {
    # read a comma-delimited list of numbers, split into a numerical array, sort, identify median
    my $numlist = shift;
    my $medval;
    
    my @vals = split /\,/, $numlist;

    if($#vals > -1) {
	my @sortedvals = sort {$a <=> $b} @vals;

	if($#vals % 2 == 0) {
	    $medval = $sortedvals[int($#vals/2)];
	} else {
	    $medval = ($sortedvals[int($#vals/2)] + $sortedvals[int($#vals/2)+1])/2;
	} 
    } else {
	$medval = ""; # -1;
    }

return $medval;   
}

sub Average {
    # read a comma-delimited list of numbers, split into a numerical array, calculate average
    my $numlist = shift;
    my $avgval;
    my $mysum = 0;
    my $mycount = 0;

    my @vals = split /\,/, $numlist;

    $mycount = $#vals + 1;
    for(my $i = 0; $i <= $#vals; $i++) {
	$mysum += $vals[$i];
    }
    if($mycount > 0) {
	$avgval = $mysum / $mycount;
    } else {
	$avgval = 0;
    }

return $avgval;   
}

sub Count {
    # read a comma-delimited list of numbers, split into a numerical array, return a count of elements
    my $numlist = shift;
    my $mycount = 0;

    my @vals = split /\,/, $numlist;

    $mycount = $#vals + 1;
    
return $mycount;   
}

sub Min {
    # read a comma-delimited list of numbers, split into a numerical array, find and return min value
    my $numlist = shift;
    my $minval;
    my $mycount;

    my @vals = split /\,/, $numlist;
    $mycount = $#vals + 1;
    if($mycount > 0) {
	$minval = $vals[0];
	for(my $i = 0; $i <= $#vals; $i++) {
	    if ($minval > $vals[$i]) {
		$minval = $vals[$i];
	    }
	}
    } else {
	$minval = -999999;
    }

return $minval;   
}

sub Max {
    # read a comma-delimited list of numbers, split into a numerical array, find and return max value
    my $numlist = shift;
    my $maxval;
    my $mycount;

    my @vals = split /\,/, $numlist;
    $mycount = $#vals + 1;
    if($mycount > 0) {
	$maxval = $vals[0];
	for(my $i = 0; $i <= $#vals; $i++) {
	    if ($maxval < $vals[$i]) {
		$maxval = $vals[$i];
	    }
	}
    } else {
	$maxval = -999999;
    }

return $maxval;   
}

sub Percentile {
    # read a value and a list of values and return the percentile of the value with respect to the list
    my ($val, $numlist) = @_;
    my $ntile = -1; # set sentinel value of -1
    my $mycount = 0;

    #print "<pre> val = $val, $numlist = $numlist</pre>\n";
    my @vals = split /\,/, $numlist;
    if($#vals > -1) {
	my @sortedvals = sort {$a <=> $b} @vals;
	$mycount = $#vals + 1;
	for(my $i = 0; $i <= $#vals; $i++) {
	    if($val >= $sortedvals[$i]) {
		$ntile = $i;
		#print "i = $i\n";
	    }
	}
	$ntile = 100 * ($ntile + 1) / $mycount;
    }
    
return $ntile;
}

1;

