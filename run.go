// todos.go
package main

import (
	"html/template"
	"net/http"
)

func main() {
	tmpl := template.Must(template.ParseFiles("/home/weertik/index.html"))
	data := struct {
		Name   string
		Github string
	}{
		Name:   "Weertik",
		Github: "https://github.com/Weertik/weertik",
	}

	http.Handle("/assets/",
		http.StripPrefix("/assets/",
			http.FileServer(http.Dir("/home/weertik/assets"))))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		tmpl.Execute(w, data)
	})

	http.ListenAndServe(":8004", nil)
}
