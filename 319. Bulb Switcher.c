int bulbSwitch(int n) {
    if (n == 0) return 0;

    int start = 1;
    int step = 2;
    int group = 1;

    while (1) {
        int end = start + step; 
        if (n >= start && n <= end)
            return group;

        start = end+1;
        step+=2;
        group++;
    }
}
