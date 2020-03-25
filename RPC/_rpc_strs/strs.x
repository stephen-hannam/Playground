/*
* date.x  Specification of the remote date and time server
*/

/*
* Define two procedures
*     bin_date_1() returns the binary date and time (no arguments)
*     str_date_1() takes a binary time and returns a string
*
*/

typedef string str<32>;
typedef str str_arr[5];

struct input_data {
  int num_strs;
  str_arr argv;
};

program STRS_PROG {
  version STRS_VERS {
    string UPPER(input_data) = 1; /* procedure number = 1 */
  } = 1;/* version number = 1 */
} = 22599;
