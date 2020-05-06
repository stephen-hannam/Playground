/*
* dir_proc.c: remote readdir
* implementation
*/

#include <dirent.h>
#include "dir.h" /* Created by rpcgen */

extern char *malloc();
extern char *strdup();

readdir_res * readdir_1(nametype *dirname, struct svc_req *req)
{
  DIR *dirp;
  struct dirent *d;
  namelist nl;
  namelist *nlp;

  static readdir_res res; /* must be static! */

  /* Open directory */
  dirp = opendir(*dirname);

 if (dirp == (DIR *)NULL) {
   return (&res);
  }

  /* Free previous result */
  xdr_free(xdr_readdir_res, &res);

  /*
   * Collect directory entries.
   * Memory allocated here is free by
   * xdr_free the next time readdir_1
   * is called
   */

   nlp = &res.readdir_res.list;
   while (d = readdir(dirp)) {
     nl = *nlp = (namenode *)
     malloc(sizeof(namenode));
     if (nl == (namenode *) NULL) {
       closedir(dirp);
       return(&res);
      }
    nl->name = strdup(d->d_name);
    nlp = &nl->next;
  }

  *nlp = (namelist)NULL;

  /* Return the result */
  closedir(dirp);
  return (&res);
}
