using System;
using System.Collections;

namespace Stopky.Models;

public class SavedTimeModel{
    public string Name{ get; }
    public TimeSpan Time{ get; }
    public DateTime Date_created{ get; }

    public SavedTimeModel(string name, TimeSpan time){
        Name = name;
        Time = time;
        Date_created = DateTime.Now;
    }
}