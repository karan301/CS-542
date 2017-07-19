use List::Util 'shuffle';

my(@d);

while(<STDIN>) {
    chomp;
    push @d, $_;
}

foreach my $i (shuffle(@d)) {
    print "$i\n";
}
