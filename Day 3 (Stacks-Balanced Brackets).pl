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
    $expression=~ s/[^\{\[\(\)\]\}]//g;
    $balanced=1;
    my @brackets=();
    foreach(my $i=0; $i <= length($expression); $i++){
        $cc=substr($expression,$i,1);
        if ($cc eq "("){
            push @brackets,")";
        }
        elsif ($cc eq "{"){
            push @brackets,"}";
        }
        elsif ($cc eq "["){
            push @brackets,"]";
        }
        else {
            my $lastb=pop @brackets;
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
