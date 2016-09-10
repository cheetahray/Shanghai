#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define BUFLEN 16
#define NPACK 1
#define PORT 9999
#define SRV_IP "192.168.12.100"
/* diep(), #includes and #defines like in the server */

void diep(char *s)
{
    perror(s);
    exit(1);
}

int main(int argc, char *argv[])
{
    struct sockaddr_in si_other;
    int s, i, slen=sizeof(si_other);
    char buf[BUFLEN];

    if ((s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP))==-1)
        diep("socket");

    memset((char *) &si_other, 0, sizeof(si_other));
    si_other.sin_family = AF_INET;
    si_other.sin_port = htons(PORT);
    if (inet_aton(SRV_IP, &si_other.sin_addr)==0) {
        fprintf(stderr, "inet_aton() failed\n");
        exit(1);
    }

    for (i=1; i<argc; i+=4) {
        sprintf(buf, "%s %s %s %s", argv[i], argv[i+1], argv[i+2], argv[i+3]);
        //printf("%s", buf);
        if (sendto(s, buf, strlen(buf), 0, (const struct sockaddr *)&si_other, slen)==-1)
            diep("sendto()");
    }

    close(s);
    return 0;
}
