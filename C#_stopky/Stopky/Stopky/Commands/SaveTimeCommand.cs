using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using Stopky.Models;
using Stopky.ViewModels;

namespace Stopky.Commands;

public class SaveTimeCommand: CommandBase{
    private readonly SaveTimeViewModel _saveTimeViewModel;

    public SaveTimeCommand(SaveTimeViewModel saveTimeViewModel){
        _saveTimeViewModel = saveTimeViewModel;
        //_saveTimeViewModel += OnViewPropertyChange;
    }
    
    public override void Execute(object? parameter){
        string json = JsonSerializer.Serialize(new SavedTimeModel(_saveTimeViewModel.SaveName, _saveTimeViewModel.SaveTime));
        File.WriteAllText(@"D:\path.json", json);
    }
}
