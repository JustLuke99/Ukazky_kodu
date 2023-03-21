using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Input;
using System.Windows.Threading;
using Stopky.Commands;
using Stopky.Stores;

namespace Stopky.ViewModels;

public class TimerViewModel: ViewModelBase{
    private string _timePassed = "00:00:00";
    private Stopwatch _timer = new Stopwatch();
    private DispatcherTimer _dispatcher = new DispatcherTimer();  

    public string TimePassed{
        get{
            return _timePassed;
        }

        set{
            _timePassed = value;
            OnPropertyChanged(nameof(TimePassed));
        }
    }
    
    public ICommand StartCommand{ get; }
    //public ICommand PauseCommand{ get; }
    public ICommand StopCommand{ get; }
    public ICommand RestartCommand{ get; }
    public ICommand SaveTimeViewCommand{ get; }

     public TimerViewModel(Stores.NavigationStore navigationStore, Func<SavedTimesListViewModel> savedTimesListViewModel, Func<SaveTimeViewModel> saveTimeViewModel){
        StartCommand = new StartTimerCommand(_timer, _dispatcher);
        RestartCommand = new StopTimerCommand(_timer, _dispatcher);
        SaveTimeViewCommand = new NavigateCommand(navigationStore, saveTimeViewModel);
            
        StopCommand = new RestartTimerCommand(_timer, _dispatcher, TimePassed);

        _dispatcher.Tick += new EventHandler(dt_Tick);  
        _dispatcher.Interval = new TimeSpan(0, 0, 0, 0, 1);
    }  

    void dt_Tick(object sender, EventArgs e){  
        if (_timer.IsRunning){  
            TimeSpan elapsed = _timer.Elapsed;  
            TimePassed = String.Format("{0:00}:{1:00}:{2:00}", elapsed.Minutes, elapsed.Seconds, elapsed.Milliseconds / 10);  
        }  
    }
}