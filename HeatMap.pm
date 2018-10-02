package My::HeatMap;
use strict;
use warnings;

use Exporter qw(import);

our @EXPORT_OK = qw(RYGHex RWGHex);

=pod

scale min..max in data to 0..255 as RGB

for 0 to 0.5, Red to Yellow
for 0.5 to 1, Yellow to Red

Red    255,   0,   0
Yellow 255, 255,   0
Green    0, 255,   0

for 0 to 0.5, Red to White
for 0.5 to 1, White to Red

Red    255,   0,   0
White  255, 255, 255
Green    0, 255,   0

=cut

sub Dec2Hex {
    my ($decval, $places) = @_;
    my $hexval;
    my $pad = '0' x $places;

    $hexval = sprintf("0x%X", $decval);
    $hexval =~ s/^0x/$pad/g;             # zero pad the hex number
    $hexval = substr $hexval, -$places;  # take the last $places characters

return $hexval;   
}

sub RYGHex {
    my ($value, $minval, $maxval) = @_;
    #print "<pre>Hi, Mom! $value, $minval, $maxval </pre>\n";
    my $scaleval = ($value - $minval)/($maxval - $minval);
    my $rdec = 255; # Default to Yellow as (255, 255, 0).
    my $gdec = 255; # Green decimal RGB value
    my $bdec = 0;   # Blue decimal RGB value
    my $hexcolor;   # Return RGB color as hex value

    if($scaleval < 0.0) {
	$rdec = 255;
	$gdec = 255;
	$bdec = 255;
    } elsif($scaleval < 0.5) {
	$rdec = 255;
	$gdec = int(2 * $scaleval * 255);
    } elsif($scaleval > 0.5) {
	$rdec = int(2 * (1 - $scaleval) * 255);
	$gdec = 255; 
    }
    $hexcolor = "#" . Dec2Hex($rdec, 2) . Dec2Hex($gdec, 2) . Dec2Hex($bdec, 2);

return $hexcolor;
}

sub RWGHex {
    my ($value, $minval, $maxval) = @_;
    #print "<pre>Hi, Mom! $value, $minval, $maxval </pre>\n";
    my $scaleval = ($value - $minval)/($maxval - $minval);
    my $rdec = 255; # Default to White as (255, 255, 255).
    my $gdec = 255; # Green decimal RGB value
    my $bdec = 255; # Blue decimal RGB value
    my $hexcolor;   # Return RGB color as hex value

    if($scaleval < 0.0) {
	$rdec = 255;
	$gdec = 255;
	$bdec = 255;
    } elsif($scaleval < 0.5) {
	$rdec = 255;
	$gdec = int(2 * $scaleval * 255);
	$bdec = int(2 * $scaleval * 255);
    } elsif($scaleval > 0.5) {
	$rdec = int(2 * (1 - $scaleval) * 255);
	$gdec = 255; 
	$bdec = int(2 * (1 - $scaleval) * 255);
    }
    $hexcolor = "#" . Dec2Hex($rdec, 2) . Dec2Hex($gdec, 2) . Dec2Hex($bdec, 2);

return $hexcolor;
}

1;

