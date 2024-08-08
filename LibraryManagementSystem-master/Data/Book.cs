using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryManagementSystem.Data
{
    public class Book
    {
        
        private long isbn;
        private string title;
        private string author;
        private string genre;
        private string description;
        private int quantity;

        public long Isbn { get => isbn; set => isbn = value; }
        public string Title { get => title; set => title = value; }
        public string Author { get => author; set => author = value; }
        public string Genre { get => genre; set => genre = value; }
        public string Description { get => description; set => description = value; }
        public int Quantity { get => quantity; set => quantity = value; }

        public Book()
        {
            
        }

        public Book(long isbn, string title, string author, string genre, string description, int quantity)
        {
            this.isbn = isbn;
            this.title = title;
            this.author = author;
            this.genre = genre;
            this.description = description;
            this.quantity = quantity;
        }

        public override string? ToString()
        {
            return $"ISBN: {isbn}\n\nTitle: {title}\nAuthor: {author}\nGenre: {genre}\nQuantity: {quantity}\nDescription: {description}";
        }
    }
}
