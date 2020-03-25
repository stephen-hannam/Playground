/*
* date.x  Specification of the remote date and time server
*/

/*
* Define two procedures
*     bin_date_1() returns the binary date and time (no arguments)
*     str_date_1() takes a binary time and returns a string
*
*/

struct input_data {
  int num_strs;
  string argv0<32>;
  string argv1<32>;
  string argv2<32>;
  string argv3<32>;
};

program STRS_PROG {
  version STRS_VERS {
    string UPPER(input_data) = 1; /* procedure number = 1 */
  } = 1;/* version number = 1 */
} = 0x31234567;/* program number = 0x31234567 */
