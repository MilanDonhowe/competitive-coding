/*
  Ok, let's be a little ambitious with C today
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/param.h>

char* readfile(const char* filename){
  FILE* f = fopen(filename, "r");
  if (f == NULL){
    fprintf(stderr, "ERR: could not open \"%s\"\n", filename);
    exit(1);
  }
  fseek(f, 0, SEEK_END);
  int file_size = ftell(f);
  fseek(f, 0, SEEK_SET);
  char* content = calloc(file_size+1, sizeof(char));
  fread(content, sizeof(char), file_size, f);
  fclose(f);
  return content;
}

struct cords {
  int x1;
  int y1;
  int x2;
  int y2;
};

struct list {
  struct list* next;
  struct cords line;
};

void free_list(struct list* ls){
  if (ls->next != NULL) free_list(ls->next);
  free(ls);
}

int part1(struct list* ls, const int ymax, const int xmax){
  // consider only vertial/horizontal lines 
  int** grid = calloc(ymax+1, sizeof(int*));
  for (int row=0; row < ymax; row++){
    grid[row] = calloc(xmax+1, sizeof(int));
  }
  
  // ok, for each horizontal or vertical line increment crossed positions
  for (struct list* iter = ls; iter->next != NULL; iter = iter->next){
    // vertical line check
    if (iter->line.x1 == iter->line.x2 && iter->line.y1 != iter->line.y2){
      // is slope increasing or decreasing?
      int dy = 1;
      if (iter->line.y2 < iter->line.y1) dy = -1;
      // check each position on the line
      for (int yi = iter->line.y1; yi != iter->line.y2 + dy; yi += dy){
        grid[yi][iter->line.x1]++;
      }
    }
    // horitzonal line check
    if (iter->line.y1 == iter->line.y2 && iter->line.x1 != iter->line.x2){
      int dx = 1;
      if (iter->line.x2 < iter->line.x1) dx = -1;
      for (int xi = iter->line.x1; xi != iter->line.x2 + dx; xi += dx){
        grid[iter->line.y1][xi]++;
      }
    }
  }

  // Determine points which overlap >= 2 times
  int overlap = 0;
  for (int yi = 0; yi < ymax; yi++){
    for (int xi = 0; xi < xmax; xi++){
      if (grid[yi][xi] > 1) overlap++;
    }
  }

  for (int i = 0; i < ymax; i++){
    free(grid[i]);
  }
  free(grid);

  return overlap;
}

// part 2 is same as part1 but now with diagonal line check
int part2(struct list* ls, const int ymax, const int xmax){
  // consider only vertial/horizontal lines 
  int** grid = calloc(ymax+1, sizeof(int*));
  for (int row=0; row < ymax; row++){
    grid[row] = calloc(xmax+1, sizeof(int));
  }
  
  // ok, for each horizontal or vertical line increment crossed positions
  for (struct list* iter = ls; iter->next != NULL; iter = iter->next){
    // vertical line check
    if (iter->line.x1 == iter->line.x2 && iter->line.y1 != iter->line.y2){
      // is slope increasing or decreasing?
      int dy = 1;
      if (iter->line.y2 < iter->line.y1) dy = -1;
      // check each position on the line
      for (int yi = iter->line.y1; yi != iter->line.y2 + dy; yi += dy){
        grid[yi][iter->line.x1]++;
      }
    }
    // horitzonal line check
    if (iter->line.y1 == iter->line.y2 && iter->line.x1 != iter->line.x2){
      int dx = 1;
      if (iter->line.x2 < iter->line.x1) dx = -1;
      for (int xi = iter->line.x1; xi != iter->line.x2 + dx; xi += dx){
        grid[iter->line.y1][xi]++;
      }
    }
    // diagonal line check (45 degrees is a linear line with slope 1)
    // so we want to check if slope is 1, i.e. x2 == x1+c & y2 == y1+c
    // if x2 - x1 == y2 - y1 then it's diagonal.
    if (abs(iter->line.y2 - iter->line.y1) == abs(iter->line.x2 - iter->line.x1)){
      int distance = abs(iter->line.x2 - iter->line.x1);
      int dx = (iter->line.x2 - iter->line.x1 > 0) ? 1 : -1;
      int dy = (iter->line.y2 - iter->line.y1 > 0) ? 1 : -1;
      for (int i = 0; i < distance+1; i++){
        grid[iter->line.y1 + (dy*i)][iter->line.x1 + (dx*i)]++;
      }
    }
  }

  // Determine points which overlap >= 2 times
  int overlap = 0;
  for (int yi = 0; yi < ymax; yi++){
    for (int xi = 0; xi < xmax; xi++){
      if (grid[yi][xi] > 1) overlap++;
    }
  }

  for (int i = 0; i < ymax; i++){
    free(grid[i]);
  }
  free(grid);
  return overlap;
}

int main(int argc, char **argv, char **envp){

  if (argc != 2) {
    printf("ERR: invalid arg count.  Proper usage: %s <input_file>", argv[0]);
    return 1;
  }

  char* problem_input = readfile(argv[1]);

  struct list* coordinates = calloc(1, sizeof(struct list));
  int n = 0; // number of coordinate pairs

  // Parse out coordinates from input into linked list
  char *saveptr = NULL;
  char *line = strtok_r(problem_input, "\n", &saveptr);
  struct list* iter = coordinates;

  int ymax = 0;
  int xmax = 0;
  while (line != NULL) {
    n++;
    // (x1, y1) -> (x2, y2)
    sscanf(line, "%d,%d -> %d, %d", &(iter->line.x1), &(iter->line.y1), &(iter->line.x2), &(iter->line.y2));
    ymax = MAX(MAX(ymax, iter->line.y1), iter->line.y2);
    xmax = MAX(MAX(xmax, iter->line.x1), iter->line.x2);

    iter->next = calloc(1, sizeof(struct list));
    iter = iter->next;
    line = strtok_r(NULL, "\n", &saveptr);
  }

  /*
    DETERMINE # POINTS WHERE MORE THAN 2 LINES OVERLAP
  
    (we're adding +1 to ymax & xmax since we also want to consider them
      as valid coordinates in our grid when we do our double for-loop.)
  */
  int overlap = part1(coordinates, ymax+1, xmax+1);
  printf("Part 1: %d\n", overlap);
  overlap = part2(coordinates, ymax+1, xmax+1);
  printf("Part 2: %d\n", overlap);
  free_list(coordinates);
  free(problem_input);
  return 0;
}