#include <stdio.h>
#include <dirent.h>
#include <errno.h>


int
main(int argc, char *argv[])
{
    DIR             *dp;
    struct dirent   *dirp;

    if (argc != 2)
        printf("Usage: ls directory_name");

    if ((dp = opendir(argv[1])) == NULL)
        printf("can't open %s", argv[1]);
    while ((dirp = readdir(dp)) != NULL)
        printf("%s\n", dirp->d_name);

    closedir(dp);
    return 0;
}
