using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using Stopky.Stores;
using Stopky.ViewModels;

namespace Stopky{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application{
        private readonly NavigationStore _navigationStore;

        public App(){
            _navigationStore = new NavigationStore();
        }
        
        protected override void OnStartup(StartupEventArgs e){
            _navigationStore.CurrentViewModel = CreateTimerViewModel();
            
            MainWindow = new MainWindowView()
            {
                DataContext = new MainWindowViewModel(_navigationStore)
            };
            MainWindow.Show();

            base.OnStartup(e);
        }

        private SavedTimesListViewModel CreateSavedTimesListViewModel(){
            return new SavedTimesListViewModel(_navigationStore, CreateTimerViewModel);
        } 
        
        private TimerViewModel CreateTimerViewModel(){
            return new TimerViewModel(_navigationStore, CreateSavedTimesListViewModel);
        }
    }
}