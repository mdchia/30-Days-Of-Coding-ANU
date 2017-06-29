#!/usr/bin/perl
use strict;
use warnings;

my $t = <STDIN>;
my $lastb;
my $cc;
my @brackets;
my $balanced;
chomp $t;

for my $a0 (0..$t-1){
    my $expression = <STDIN>;
    chomp $expression;
    $expression=~ s/[^\{\[\(\)\]\}]//g; # strip things that aren't brackets
    $balanced=1; # assume it's balanced until we find otherwise
    my @brackets=();
    foreach(my $i=0; $i <= length($expression); $i++){
        $cc=substr($expression,$i,1);
        if ($cc eq "("){ # push the opposite bracket because we'll compare later
            push @brackets,")";
        }
        elsif ($cc eq "{"){
            push @brackets,"}";
        }
        elsif ($cc eq "["){
            push @brackets,"]";
        }
        else {
            my $lastb=pop @brackets; # do the actual comparison on the way back
            if($cc ne $lastb){
                $balanced=0;
            }
        }
    }
    if ($balanced){
        print "YES\n";
    } else {
        print "NO\n";
    }
    #print $a0;
    #print @brackets,"\n";
}
