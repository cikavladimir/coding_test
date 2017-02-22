package main

import (
  "bufio"
  "os"
  "fmt"
  "sort"
  "strings"
  "strconv"
)

// Initialize variables 
var min map[string]int
var max map[string]int
var count map[string]int
var total map[string]int


func main() {
  fmt.Println(os.Args[1])
  host := ""
  temp_minute := "-1"
  temp_time := ""
  current_minute := "-1"
  service_integer := -1
  min = make(map[string]int)
  max = make(map[string]int)
  count = make(map[string]int)
  total = make(map[string]int)
  
  // Notes: 25sec to read each line in 18,227,200 lines and iterate trough array.
  // Notes: 1min and 14sec to read each line in 18,227,200 lines and apply all the logic.
  if file, err := os.Open(os.Args[1]); err == nil {
  // if file, err := os.Open("tiny.txt"); err == nil {

    // make sure it gets closed
    defer file.Close()

    // create a new scanner and read the file line by line
    scanner := bufio.NewScanner(file)

    // Read line by line:
    for scanner.Scan() {
      arr := strings.Split(scanner.Text(), " ")
      a := "";

      date_time := arr[0][0:16]
      current_minute = arr[0][14:16]

      for _, element := range arr {
        a = element
        element = a
        
        if strings.Contains(element, "host") {
          host_array := strings.Split(element, "=")
          host = strings.Replace(host_array[1], "\"", "", -1)
        }

        if strings.Contains(element, "service") {
          service_array := strings.Split(element, "=")
          service := strings.Replace(service_array[1], "ms", "", -1)
          service_integer, _ = strconv.Atoi(service)
        }
      }

      // Check if is a first line:
      if (temp_minute == "-1") {
        min[host] = service_integer
        max[host] = service_integer
        count[host] = 1
        total[host] = service_integer
      } else if (temp_minute != current_minute) {
        var keys []string
        for k := range min {
          keys = append(keys, k)
        }
        sort.Strings(keys)
        for _, k := range keys {
            // fmt.Printf("%v:00,%v,%v,%v,%v,%v\n", temp_time,k,count[k],total[k],min[k],max[k])
            count[k] = 0
            total[k] = 0
            min[k] = 0
            max[k] = 0
        }

        min[host] = service_integer
        max[host] = service_integer
        count[host] = 1
        total[host] = service_integer
      } else {
        if _, ok := min[host]; ok {
              if (min[host] == 0) {
                min[host] = service_integer
              }
              if (min[host] > service_integer) {
                min[host] = service_integer
              }
              if (max[host] < service_integer) {
                max[host] = service_integer
              }
              count[host] = count[host] + 1
              total[host] = total[host] + service_integer
          } else {
            min[host] = service_integer
            max[host] = service_integer
            count[host] = 1
            total[host] = service_integer
          }
      }

      temp_minute = current_minute
      temp_time = date_time
    }

    // check for errors
    if err = scanner.Err(); err != nil {
    }

  } else {
    // log.Fatal(err)
  }

  // Check last line:
  if (temp_minute == current_minute) {
        var keys []string
        for k := range min {
          keys = append(keys, k)
        }
        sort.Strings(keys)
        for _, k := range keys {
            fmt.Printf("%v:00,%v,%v,%v,%v,%v\n", temp_time,k,count[k],total[k],min[k],max[k])
        }
  }

}