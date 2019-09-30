public class Problem19 {
    public static void main (String[] args) {
        // Date date = new Date(3);
        // Date date2 = new Date(368);
        // Date date3 = new Date (555555);
        // print(date);
        // print(date2);
        // print(date3);
        findFirstSundays();
    }

    public static void findFirstSundays() {
        int sum = 0;
        int daysFromJan1st1900 = 365;
        boolean finished = false;
        while (!finished) {
            Date date = new Date(daysFromJan1st1900);
            System.out.println(daysFromJan1st1900);
            System.out.println("Checking: "+date.dayOfMonth+"/"+date.month+"/"+date.year);
            if (date.year > 2000) finished=true;
            if (date.dayOfMonth==1 && date.dayOfWeek == 7) sum++;
            daysFromJan1st1900++;
        }
        System.out.println(sum);
        
    }

    private static void print(Date date) {
        System.out.println("Days from 1/1/1990:");
        System.out.println("     "+date.daysFromJan1st1900);
        System.out.println("Year:");
        System.out.println("     "+date.year);
        System.out.println("Day of the year:");
        System.out.println("     "+date.dayOfYear);
        System.out.println("Month:");
        System.out.println("     "+date.month);
        System.out.println("Day of Month:");
        System.out.println("     "+date.dayOfMonth);
        System.out.println("Day of Week:");
        System.out.println("     "+date.dayOfWeek);
        System.out.println();
    }
}

class Date {
    int year, dayOfYear, month, dayOfMonth, week, dayOfWeek, daysFromJan1st1900;

    Date (int daysFromJan1st1900) {
        this.daysFromJan1st1900 = daysFromJan1st1900;
        year = whichYear(daysFromJan1st1900);
        dayOfYear = whichDayOfYear(daysFromJan1st1900);
        month = whichMonth(dayOfYear, year);
        dayOfMonth = whichDayOfMonth(dayOfYear, year);
        dayOfWeek = whichDayOfWeek(daysFromJan1st1900);
    }

    int whichDayOfMonth(int givenDayOfYear, int givenYear) {
        int monthCandidate = 1;
        int limit = 0;
        while (true) {
            limit += daysInMonth(monthCandidate, givenYear);
            if (dayOfYear <= limit) {
                int remainder = -1*(givenDayOfYear-limit);
                return daysInMonth(monthCandidate, givenYear) - remainder;
            }
            monthCandidate++;
        }
    }

    boolean isLeapYear (int givenYear) {
        if (givenYear % 4 == 0) {
            if (givenYear % 100 == 0) {
                if (givenYear % 400 == 0) {
                    return true;
                }
            } else {
                return true;
            }
        }
        return false;
    }

    int whichDayOfYear (int daysFromJan1st1900) {
        int yearCandidate = 1900;
        int limit = 0;
        while (true) {
            limit += daysInYear(yearCandidate);
            if (daysFromJan1st1900 <= limit) {
                int remainder = -1*(daysFromJan1st1900-limit);
                return daysInYear(yearCandidate) - remainder;
            } else {
                yearCandidate++;
            }
        }
    }

    int daysInYear(int givenYear) {
        if (isLeapYear(givenYear)) {
            return 366;
        } else {
            return 365;
        }
    }

    int daysInMonth(int givenMonth, int givenYear) {
        if (givenMonth == 1) {
            return 31;
        } else if (givenMonth == 2) {
            if (isLeapYear(givenYear)) {
                return 29;
            } else {
                return 28;
            }
        } else if (givenMonth == 3) {
            return 31;
        } else if (givenMonth == 4) {
            return 30;
        } else if (givenMonth == 5) {
            return 31;
        } else if (givenMonth == 6) {
            return 30;
        } else if (givenMonth == 7) {
            return 31;
        } else if (givenMonth == 8) {
            return 31;
        } else if (givenMonth == 9) {
            return 30;
        } else if (givenMonth == 10) {
            return 31;
        } else if (givenMonth == 11) {
            return 30;
        } else if (givenMonth == 12) {
            return 31;
        }
        return 0;
    }

    int whichDayOfWeek(int daysFromJan1st1900) {
        return daysFromJan1st1900 % 7 + 1;
    }

    int whichYear (int daysFromJan1st1900) {
        int yearCandidate = 1900;
        int limit = 0;
        while (true) {
            limit += daysInYear(yearCandidate);
            if (daysFromJan1st1900 <= limit) {
                return yearCandidate;
            } else {
                yearCandidate++;
            }
        }
    }

    int whichMonth(int dayOfYear, int givenYear) {
        int monthCandidate = 1;
        int limit = 0;
        while (true) {
            limit += daysInMonth(monthCandidate, givenYear);
            if (dayOfYear <= limit) {
                return monthCandidate;
            }
            monthCandidate++;
        }
    }
}
