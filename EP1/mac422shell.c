#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>


#define MAX_LENGTH 1024
#define DELIMS " \t\r\n"

int protegepracaramba(char* file);
int liberageral(char* file);
void rodeveja(char* file);
void rode(char* file);

int main(int argc, char *argv[]) {
  char *cmd;
  char line[MAX_LENGTH];

  while (1) {
    printf("$ ");
    if (!fgets(line, MAX_LENGTH, stdin)) break;

    /*Parse */
    if ((cmd = strtok(line, DELIMS))) {
		errno = 0;

		/*--- PROTEGEPRACARAMBA ---*/
		if (strcmp(cmd, "protegepracaramba") == 0) {
			char *arg = strtok(0, DELIMS);

			if (!arg) fprintf(stderr, "[ERRO] este comando precisa de argumento\n");
			else protegepracaramba(arg);

		}

		/*--- PROTEGEPRACARAMBA ---*/
		else if (strcmp(cmd, "liberageral") == 0) {
			char *arg = strtok(0, DELIMS);

			if (!arg) fprintf(stderr, "[ERRO] este comando precisa de argumento\n");
			else liberageral(arg);

		} 

		/*--- RODEVEJA ---*/
		else if (strcmp(cmd, "rodeveja") == 0) {
			char *arg = strtok(0, DELIMS);

			if (!arg) fprintf(stderr, "[ERRO] este comando precisa de argumento\n");
			else rodeveja(arg);
		}

		/*--- RODE ---*/
		else if (strcmp(cmd, "rode") == 0) {
			char *arg = strtok(0, DELIMS);

			if (!arg) fprintf(stderr, "[ERRO] este comando precisa de argumento\n");
			else rode(arg);
		}

		/*Sai do programa se o comando nao existir*/
		else 
			break;

  		if (errno) perror("Command failed");
    }
  }

  return 0;
}

int protegepracaramba(char* file) 
{
	return chmod(file, 00000);
}

int liberageral(char* file)
{
	return chmod(file, 00777);
}

void rodeveja(char* file) 
{
	pid_t child_pid = fork();
	int status, i;

	/* Em caso de falha de fork */
	if (child_pid == -1) {
		printf("O programa falhou no fork()\n");
		exit(EXIT_FAILURE); 
	} 

	/*Bloco executado pelo child*/
	else if (child_pid == 0)
		execve(file, NULL, NULL);

	/*Bloco executado pelo pai*/
	else {
		wait(&status);
		printf("=> programa '%s' retornou com codigo %d.\n", file, status);
	}

}

void rode (char* file) 
{
	pid_t child_pid = fork();
	int status, i;

	/*Em caso de falha de fork*/
	if (child_pid == -1) {
		printf("O programa falhou no fork()\n");
		exit(EXIT_FAILURE); 
	} 

	/*Bloco executado pelo child*/
	else if (child_pid == 0)
		execve(file, NULL, NULL);
}
