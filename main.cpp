#include <stdio.h>
#include <stdbool.h>

#define P 5 // Number of processes
#define R 3 // Number of resources

void calculateNeed(int need[P][R], int max[P][R], int alloc[P][R]) {
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < R; j++) {
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }
}

bool isSafe(int processes[], int avail[], int max[][R], int alloc[][R]) {
    int need[P][R];
    calculateNeed(need, max, alloc);

    bool finish[P] = {false};
    int safeSeq[P];
    int work[R];
    for (int i = 0; i < R; i++) {
        work[i] = avail[i];
    }

    int count = 0;
    while (count < P) {
        bool found = false;
        for (int p = 0; p < P; p++) {
            if (!finish[p]) {
                bool canAllocate = true;
                for (int j = 0; j < R; j++) {
                    if (need[p][j] > work[j]) {
                        canAllocate = false;
                        break;
                    }
                }
                if (canAllocate) {
                    for (int k = 0; k < R; k++) {
                        work[k] += alloc[p][k];
                    }
                    safeSeq[count++] = p;
                    finish[p] = true;
                    found = true;
                }
            }
        }
        if (!found) {
            printf("The system is in an unsafe state.\n");
            return false;
        }
    }

    printf("The system is in a safe state.\nSafe Sequence: ");
    for (int i = 0; i < P; i++) {
        printf("P%d ", safeSeq[i]);
    }
    printf("\n");
    return true;
}

int main() {
    int processes[] = {0, 1, 2, 3, 4};
    int available[] = {3, 3, 2};
    int max[P][R] = {{7, 5, 3}, {3, 2, 2}, {9, 0, 2}, {2, 2, 2}, {4, 3, 3}};
    int allocation[P][R] = {{0, 1, 0}, {2, 0, 0}, {3, 0, 2}, {2, 1, 1}, {0, 0, 2}};

    isSafe(processes, available, max, allocation);
    return 0;
}
