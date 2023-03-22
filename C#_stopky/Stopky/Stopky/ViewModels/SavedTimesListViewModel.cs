using System;
using System.Collections.Generic;
using System.IO;
using System.Windows.Input;
using Newtonsoft.Json;
using Stopky.Commands;
using Stopky.Models;

namespace Stopky.ViewModels;

public class SavedTimesListViewModel: ViewModelBase{
    private readonly IEnumerable<SavedTimeModel>? _savedTimes;
    public IEnumerable<SavedTimeModel>? SavedTimes => _savedTimes;
    public ICommand BackCommand{ get; }
    
    public SavedTimesListViewModel(Stores.NavigationStore navigationStore, Func<TimerViewModel> timerViewModel){
        BackCommand = new NavigateCommand(navigationStore, timerViewModel);

        var data = File.ReadAllText(@"save.json");
        _savedTimes = JsonConvert.DeserializeObject<List<SavedTimeModel>>(data);
    }
}