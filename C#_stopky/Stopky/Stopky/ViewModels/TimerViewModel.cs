using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Windows.Input;
using System.Windows.Threading;
using Microsoft.Toolkit.Mvvm.Input;
using Newtonsoft.Json;
using Stopky.Commands;
using Stopky.Models;

namespace Stopky.ViewModels;

public class TimerViewModel: ViewModelBase{
    private string _timePassed = "00:00:00";
    private string _saveName = "";
    private Stopwatch _timer = new Stopwatch();
    private DispatcherTimer _dispatcher = new DispatcherTimer();
    private string _startV = "Visible";
    private string _pauseV = "hidden";
    private string _stopV = "hidden";
    private string _restartV = "hidden";
    private string _saveV = "hidden";
    private string _boxV = "hidden";
    private string _save2 = "hidden";

    public string SaveName{
        get{ return _saveName; }
        set{ _saveName = value;
            OnPropertyChanged(nameof(SaveName)); }
    }
    
    public string TimePassed{
        get{ return _timePassed; }
        set{ _timePassed = value;
            OnPropertyChanged(nameof(TimePassed)); }
    }
    
    public string StartV{
        get{ return _startV; }
        set{ _startV = value;
            OnPropertyChanged(nameof(StartV)); }
    }
    
    public string PauseV{
        get{ return _pauseV; }
        set{ _pauseV = value;
            OnPropertyChanged(nameof(PauseV)); }
    }
    
    public string StopV{
        get{ return _stopV; }
        set{ _stopV = value;
            OnPropertyChanged(nameof(StopV)); }
    }
    
    public string RestartV{
        get{ return _restartV; }
        set{ _restartV = value;
            OnPropertyChanged(nameof(RestartV)); }
    }
    
    public string SaveV{
        get{ return _saveV; }
        set{ _saveV = value;
            OnPropertyChanged(nameof(SaveV)); }
    }
    
    public string BoxV{
        get{ return _boxV; }
        set{ _boxV = value;
            OnPropertyChanged(nameof(BoxV)); }
    }
    
    public string Save2{
        get{ return _save2; }
        set{ _save2 = value;
            OnPropertyChanged(nameof(Save2)); }
    }

    public ICommand StartCommand{ get; }
    public ICommand PauseCommand{ get; }
    public ICommand StopCommand{ get; }
    public ICommand RestartCommand{ get; }
    public ICommand SaveCommand{ get; }
    public ICommand SaveTimeCommand{ get; }
    public ICommand SaveTimeViewCommand{ get; }

     public TimerViewModel(Stores.NavigationStore navigationStore, Func<SavedTimesListViewModel> savedTimesListViewModel){
         
        StartCommand = new RelayCommand(StartTimer);
        RestartCommand = new RelayCommand(RestartTimer);
        StopCommand = new RelayCommand(StopTimer);
        PauseCommand = new RelayCommand(PauseTimer);
        SaveCommand = new RelayCommand(ShowSave);
        SaveTimeCommand = new RelayCommand(SaveTime);
        
        SaveTimeViewCommand = new NavigateCommand(navigationStore, savedTimesListViewModel);
        
        _dispatcher.Tick += new EventHandler(dt_Tick);  
        _dispatcher.Interval = new TimeSpan(0, 0, 0, 0, 1);
    }  

    void dt_Tick(object sender, EventArgs e){  
        if (_timer.IsRunning){  
            TimeSpan elapsed = _timer.Elapsed;  
            TimePassed = String.Format("{0:00}:{1:00}:{2:00}", elapsed.Minutes, elapsed.Seconds, elapsed.Milliseconds / 10);  
        }  
    }

    private void StartTimer(){
        _timer.Start();  
        _dispatcher.Start();
        PauseV = "Visible";
        StopV = "hidden";
        RestartV = "hidden";
        StartV = "hidden";
    }
    
    private void PauseTimer(){
        if (_timer.IsRunning){  
            _timer.Stop();  
        }
        PauseV = "hidden";
        StopV = "Visible";
        StartV = "Visible";
    }
    
    private void StopTimer(){
        StartV = "hidden";
        StopV = "hidden";
        RestartV = "Visible";
        SaveV = "Visible";
    }
    
    private void RestartTimer(){
        _timer.Stop();
        _timer.Reset();
        TimePassed = "00:00:00";
        RestartV = "hidden";
        StartV = "Visible";
        SaveV = "hidden";
    }
    
    private void ShowSave(){
        BoxV = "Visible";
        Save2 = "Visible";
        SaveV = "hidden";
        SaveName = "";
    }

    private void SaveTime(){
        string filename = @"save.json";

        if (File.Exists(filename) == false){
            var data = JsonConvert.SerializeObject(new SavedTimeModel(SaveName, TimePassed));
            File.WriteAllText(filename, data);
        }else{
            var data = File.ReadAllText(filename);
            var desData = JsonConvert.DeserializeObject<List<SavedTimeModel>>(data);
            List<SavedTimeModel> forSave = new List<SavedTimeModel>();
            if (desData is not null){
                forSave.AddRange(desData);
            }
            forSave.Add(new SavedTimeModel(SaveName, TimePassed));

            var json = Newtonsoft.Json.JsonConvert.SerializeObject(forSave);
            File.WriteAllText(filename, json);
        }

        BoxV = "hidden";
        Save2 = "hidden";
    }
}