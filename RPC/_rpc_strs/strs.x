/*
* date.x  Specification of the remote date and time server
*/

/*
* Define two procedures
*     bin_date_1() returns the binary date and time (no arguments)
*     str_date_1() takes a binary time and returns a string
*
*/

program STRS_PROG {
  version STRS_VERS {
    string UPPER(string) = 1; /* procedure number = 1 */
  } = 1;/* version number = 1 */
} = 0x31234567;/* program number = 0x31234567 */
